from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # Simple session logic as requested
        if username in ['murali', 'nikhil']:
             request.session['username'] = username
             return redirect('home')
        else:
             return render(request, 'accounts/login.html', {'error': 'Invalid username. Please use "murali" or "yashu".'})
    return render(request, 'accounts/login.html')

def home_view(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    
    role_text = ""
    if username == 'Boss':
        role_text = "You're the owner"
    elif username == 'nikhilbabu':
        role_text = "You're the employee"
        
    return render(request, 'accounts/home.html', {'role_text': role_text, 'username': username})

def about_view(request):
    return render(request, 'accounts/about.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

def logout_view1(request):
    request.session.flush()
    return redirect('login')
