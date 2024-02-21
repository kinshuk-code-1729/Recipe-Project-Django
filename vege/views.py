from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_desc = data.get("recipe_desc")
        recipe_image = request.FILES.get('recipe_image')
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_desc = recipe_desc,
            recipe_image = recipe_image
        )
        return redirect("/recipes/")
        # print(f"Recipe Name : {recipe_name}, Description : {recipe_desc} , Image : {recipe_image}")
        
    querySet = Recipe.objects.all()
    
    if request.GET.get('search'):
        querySet = querySet.filter(recipe_name__icontains = request.GET.get('search'))
        
    context = {'recipes' : querySet , 'page' : 'Recipes Home'}
        
    return render(request,"recipes.html",context)

def delete_recipe(request, id):
    # print(id)
    querySet = Recipe.objects.get(id = id)
    querySet.delete()
    return redirect("/recipes/")

def update_recipe(request, id):
    querySet = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_desc = data.get("recipe_desc")
        
        querySet.recipe_name = recipe_name
        querySet.recipe_desc = recipe_desc
        
        if recipe_image:
            querySet.recipe_image = recipe_image
            
        querySet.save()
        return redirect('/recipes/')
            
    context = {"recipe" : querySet, 'page' : 'Update Recipe'}
    return render(request,"update_recipes.html",context)

def login_page(request):
    return render(request, 'login.html' , context = {'page' : 'Login Page'})

def register(request):
    return render(request, 'register.html', context = {'page' : 'Sign Up Page'})