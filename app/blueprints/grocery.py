from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import GroceryItem
from app.extensions import db
from app.forms import GroceryForm

grocery_bp = Blueprint('grocery', __name__, template_folder='../templates')

@grocery_bp.route('/grocery_list', methods=['GET', 'POST'])
def manage_grocery():
    form = GroceryForm()
    if form.validate_on_submit():
        item = GroceryItem(
            name=form.name.data,
            quantity=form.quantity.data,
            unit=form.unit.data,
            price=form.price.data
        )
        db.session.add(item)
        db.session.commit()
        flash('Grocery item added successfully.')
        return redirect(url_for('grocery.manage_grocery'))
    
    grocery_items = GroceryItem.query.all()
    return render_template('grocery.html', form=form, grocery=grocery_items)

@grocery_bp.route('/grocery_list/delete/<int:item_id>', methods=['POST'])
def delete_grocery_item(item_id):
    item = GroceryItem.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully.')
    return redirect(url_for('grocery.manage_grocery'))

