from .cart import Cart

# xử lý ngữ cảnh để giỏ hàng có thể hoạt động trên tất cả các trang của trang web
def cart(request):
	# Return the default data from Cart
	return {'cart': Cart(request)}