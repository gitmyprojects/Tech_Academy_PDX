from django.db import models

# The first element in each tuple is the actual value to be set on the model, and the second element is
# the human-readable name.
cat_choices = [
    ('breakfast','breakfast'),
    ('snack','snack'),
    ('dessert','dessert'),
    ('fast-food','fast-food'),
    ('sandwich','sandwich'),
    ('candy','candy'),
    ('beverage','beverage')
]

# what do you need to know about this object?
# by default, django sees the fields as required unless 'required' is set to False.
class Item(models.Model):
    item_name = models.CharField(max_length=20, default="")
    item_category = models.CharField(max_length=20, default="", choices=cat_choices)
    description = models.TextField(default="")

    items = models.Manager()

# the following is what tells the site what to show once the item is added.
    def __str__(self):
        return self.item_name
