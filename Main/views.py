from django.shortcuts import render,HttpResponse,redirect
from .models import Agent,Property,Image,Amenities,Post,postComments,Contact
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def index(request):
    blogs=Post.objects.all().order_by("-date")[0:4]
    
    agents=Agent.objects.all().order_by("-id")[0:3]
    
    properties=Property.objects.all().order_by("-price")[0:4]
    
    images=[]
    
    for p in properties:
        img=Image.objects.filter(property_id=p.id).first()
        images.append(img)
    data=zip(properties,images)
    
    prop=Property.objects.all().order_by("-area")[0:4]
    
    img=[]
    
    for p in prop:
        i=Image.objects.filter(property_id=p.id).first()
        img.append(i)
    main=zip(prop,img)
    
    
    
    
    
    
    
    return render(request,'index.html',{"blogs":blogs,"agents":agents,"data":data,"main":main})

def about(request):
    agents=Agent.objects.all().order_by("-id")[0:3]
    return render(request,"about.html",{"agents":agents})

def agent(request,pk):
    info=Agent.objects.get(id=pk)
    property=Property.objects.filter(agent_id=pk)
    count=property.count
    images=[]
    
    for p in property:
        img=Image.objects.filter(property_id=p.id).first()
        images.append(img)
    data=zip(property,images)
    
    return render(request,"agent-single.html",{"info":info,"data":data,"count":count})

def agentGrid(request):
    agents=Agent.objects.all()
    page=Paginator(agents,6)
    
    page_list=request.GET.get('page')
    page=page.get_page(page_list)
    return render(request,"agents-grid.html",{"page":page})

def blog(request,pk):
    data=Post.objects.get(id=pk)
    comments=postComments.objects.filter(post_id=pk)
    count=comments.count()
    return render(request,"blog-single.html",{"data":data,"comments":comments,"count":count})

def blogGrid(request):
    data=Post.objects.all()
    page=Paginator(data,6)
    
    page_list=request.GET.get('page')
    
    
    page=page.get_page(page_list)
    
        
    return render(request,"blog-grid.html",{"page":page})

def prop(request,pk):
    prop_info=Property.objects.get(id=pk)
    img=Image.objects.filter(property_id=prop_info.id)
    ajant=Agent.objects.get(id=prop_info.agent_id)
    
    return render(request,"property-single.html",{'data':prop_info,"images":img,"ajant":ajant})

def propertyGrid(request):
    
    property=Property.objects.all()
    
    page=Paginator(property,6)
    
    page_list=request.GET.get('page')
    page=page.get_page(page_list)
    
    images=[]
    
    for p in page.object_list:
        img=Image.objects.filter(property_id=p.id).first()
        images.append(img)
    info=zip(page.object_list,images)
    
    
    
    return render(request,"property-grid.html",{"info":info,"page":page})

def contact(request):
    
    
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        
        obj=Contact()
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()
        messages.success(request,"Form submitted successfully")
        
        
        
    
        
    return render(request,"contact.html")

def comment(request):
    
    if request.method=="POST":
        
        Name=request.POST.get("Name")
        email=request.POST.get("Email")
        blogID=request.POST.get("blogID")
        content=request.POST.get("message")
        obj=postComments()
        obj.naam=Name
        obj.email=email
        obj.post_id=blogID
        obj.comment=content
        obj.save()
        return redirect('blog',blogID) 
    return HttpResponse("galt jagah a geya")

def searchFilter(request):
    if request.method=="POST":
        keyword=request.POST.get("keyword") 
        category=request.POST.get("category") 
        city=request.POST.get("city") 
        bedroomsQuery=request.POST.get("bedrooms",None) 
        garagesQuery=request.POST.get("garages",None) 
        bathroomsQuery=request.POST.get("bathrooms",None) 
        
        priceQuery=request.POST.get("price",None)
        
        if priceQuery:
            price=request.POST.get("price",None)
            
        else:
            price=0
            
        if bathroomsQuery:
            bathrooms=request.POST.get("bathrooms")
            
        else:
            bathrooms=0
        
        if garagesQuery:
            garages=request.POST.get("garages")
            
        else:
            garages=0
        
        if bedroomsQuery:
            bedrooms=request.POST.get("bedrooms")
            
        else:
            bedrooms=0
            
        property=Property.objects.filter(prop_name__icontains=keyword, status__icontains=category, location__icontains=city, beds__gte=bedrooms,garage__gte=garages,baths__gte=bathrooms,price__gte=price)
        
        
    
        page=Paginator(property,6)
        
        page_list=request.GET.get('page')
        page=page.get_page(page_list)
        
        images=[]
        
        for p in page.object_list:
            img=Image.objects.filter(property_id=p.id).first()
            images.append(img)
        info=zip(page.object_list,images)
        
        return render(request,"property-grid.html",{"info":info,"page":page})
        
        
        
        
        
    return HttpResponse("success")


def filter(request):
    if request.method=="POST":
        category=request.POST.get("category") 
        print("category")
        print(category)
        
        property=Property.objects.filter(status__icontains=category)
        
        page=Paginator(property,6)
        
        page_list=request.GET.get('page')
        page=page.get_page(page_list)
        
        images=[]
        
        for p in page.object_list:
            img=Image.objects.filter(property_id=p.id).first()
            images.append(img)
        info=zip(page.object_list,images)
        
        return render(request,"property-grid.html",{"info":info,"page":page})
     
    return HttpResponse("success")    