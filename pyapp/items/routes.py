from flask import Blueprint, render_template, flash, url_for, request, redirect

from pyapp.items.forms import ItemForm, ItemUpdateForm, SearchForm
from pyapp.items.utils import save_image
from pyapp.models import StoreItem
from pyapp import db

items = Blueprint('items', __name__)


@items.route('/item/new', methods=['GET', 'POST'])
def add_item():

    form = ItemForm()
    if form.validate_on_submit():
        if form.image.data:
            image = save_image(form.image.data)
            item = StoreItem(name=form.name.data, price=form.price.data, image=image, sale=0)
            db.session.add(item)
            db.session.commit()
            flash('Item successfully added!', 'success')
        else:
            item = StoreItem(name=form.name.data, price=form.price.data, image='default_item.jpg', sale=0)
            db.session.add(item)
            db.session.commit()
            flash('Item successfully added!', 'success')
    return render_template('add_item.html', form=form)


@items.route('/item/view_all', methods=['GET', 'POST'])
def view_items():
    form = SearchForm()
    if form.clear.data:
        page = request.args.get('page', 1, type=int)
        items = StoreItem.query.paginate(page=page, per_page=16)
        form.query.data = ''
        return render_template('items.html', items=items, form=form)
    if form.submit.data:
        query = form.query.data
        page = request.args.get('page', 1, type=int)
        items = StoreItem.query.filter(StoreItem.name.contains(query)).paginate(page=page, per_page=16)
        sort_by = form.sort.data
        if sort_by == 'name-za':
            page = request.args.get('page', 1, type=int)
            items = StoreItem.query.filter(StoreItem.name.contains(query)).order_by(StoreItem.name.desc()).paginate(page=page, per_page=16)
            return render_template('items.html', items=items, form=form)
        elif sort_by == 'name-az':
            page = request.args.get('page', 1, type=int)
            items = StoreItem.query.filter(StoreItem.name.contains(query)).order_by(StoreItem.name.asc()).paginate(
                page=page, per_page=16)
            return render_template('items.html', items=items, form=form)
        elif sort_by == 'price-hl':
            page = request.args.get('page', 1, type=int)
            items = StoreItem.query.filter(StoreItem.name.contains(query)).order_by(StoreItem.price.desc()).paginate(page=page, per_page=16)
            return render_template('items.html', items=items, form=form)
        elif sort_by == 'price-lh':
            page = request.args.get('page', 1, type=int)
            items = StoreItem.query.filter(StoreItem.name.contains(query)).order_by(StoreItem.price.asc()).paginate(page=page, per_page=16)
            return render_template('items.html', items=items, form=form)
        elif sort_by == 'sale':
            page = request.args.get('page', 1, type=int)
            items = StoreItem.query.filter(StoreItem.name.contains(query)).order_by(StoreItem.sale.desc()).paginate(page=page, per_page=16)
            return render_template('items.html', items=items, form=form)
    else:
        page = request.args.get('page', 1, type=int)
        items = StoreItem.query.order_by(StoreItem.price.desc()).paginate(page=page, per_page=16)
        return render_template('items.html', items=items, form=form)


@items.route('/item/<int:item_id>', methods=['GET'])
def item(item_id):
    item = StoreItem.query.get_or_404(item_id)
    return render_template('item.html', item=item)


@items.route('/item/<int:item_id>/update', methods=['GET', 'POST'])
def update_item(item_id):
    item = StoreItem.query.get_or_404(item_id)
    # if item.author != current_user:
    #     abort(403)
    form = ItemUpdateForm()
    if form.validate_on_submit():
        if form.image.data:
            item.image = save_image(form.image.data)
            item.name = form.name.data
            item.price = form.price.data
            item.sale = form.percentage_off.data
            db.session.commit()
            flash('Item successfully updated!', 'success')
            return redirect(url_for('items.item', item_id=item.id))
        else:
            item.name = form.name.data
            item.price = form.price.data
            item.sale = form.percentage_off.data
            db.session.commit()
            flash('Item successfully updated!', 'success')
            return redirect(url_for('items.item', item_id=item.id))
    elif request.method == 'GET':
        form.name.data = item.name
        form.price.data = item.price
        form.percentage_off.data = item.sale
        form.image.data = item.image
    return render_template('update_item.html', title='Update Item', legend='Update Item', form=form)


