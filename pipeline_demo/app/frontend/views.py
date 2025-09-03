from django.shortcuts import render

# Existing home view
def home(request):
    return render(request, 'index.html')

# New test view
def test(request):
    return render(request, 'test.html')  # We'll create this 'test.html' file next
