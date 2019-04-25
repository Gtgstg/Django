from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.views.decorators import csrf
class BstNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else:
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)
arr=[]
brr=[]
b=BstNode(100000000000000000)
def loggedin(request):
	c=[]
	for i in range(0,len(brr),2):
		c.append(brr[i])
	return render(request,'loggedin.html',{'brr':c})
def about(request):
	username=int(request.POST.get('username',''))
	b.insert(username)
	return render(request,'index.html')
def logout(request):
	global brr
	aaa=[]
	lines, _, _, _ = _display_aux(b)
	for l in range(2,len(lines)):
		print(lines[l])
		aaa.append(lines[l])
	brr=[0]*(len(lines)-1)
	for i in range(2,len(lines),2):
		xo=lines[i].split()
		for j in range(0,len(xo)):
			brr[i-2]+=int(xo[j].strip("_"))	
	return render(request,'logout.html',{'aaa':aaa})
def index(request):
	return render(request,'index.html')	
def login(request):
	return render(request,'login.html')
def	auth_view(request):
	username=request.POST.get('username','')
	arr.append(username)
	return render(request,'login.html')
def success(request):
	quickSort(arr,0,len(arr)-1)
	return render(request,'success.html',{'arr':arr})
def register_user(request):
	return render(request,'register.html')
def partition(arr,low,high): 
    i = ( low-1 )      
    pivot = arr[high]  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
def _display_aux(b):
        if b.right is None and b.left is None:
            line = '%s' % b.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        if b.right is None:
            lines, n, p, x = _display_aux(b.left)
            s = '%s' % b.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if b.left is None:
            lines, n, p, x = _display_aux(b.right)
            s = '%s' % b.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        left, n, p, x = _display_aux(b.left)
        right, m, q, y = _display_aux(b.right)
        s = '%s' % b.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
