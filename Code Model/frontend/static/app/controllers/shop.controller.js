mainApp.controller("ShopController", ['$scope','$http', function($scope,$http) {
	// Dummy Data
	$scope.products = [{'id': '1', 'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/shop/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/shop/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/shop/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}]

	$scope.product = {'id': '1', 'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/shop/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'};

	$scope.categories = [{'title': 'Tech', 'description': 'Tech Description', 'product_count': '152', 'primary_image': 'static/img/100x100.png'}, {'title': 'Home', 'description': 'Home Description', 'product_count': '100', 'primary_image': 'static/img/100x100.png'}];
	$scope.category_tree = [{'parent': 'Tech', 'children': [{'parent': 'Laptops', 'children': ['Mac', 'Ultra Books']}]}]

	$scope.tags = ['New Season', 'Watches', 'Classic'];
	$scope.promotions = [{'title': 'Save up to $150 on Your Next Laptop', 'description': 'I\'m Not Gonna Pay A Lot For This Laptop.', 'btn_link': '/#', 'btn_text': 'Shop Now', 'is_banner': 'true', 'primary_image': 'static/img/test_slider/1-i.png'}];

	$scope.store = [{'primary_logo': 'static/img/logo-w.png', 'name': 'TheStore', 'description': 'Store in a box'}];

	var cart_items = [{'price': '13', 'quantity': '1', 'title': 'Gucci Patent Leather Open Toe Platform', 'item_link': '#/', 'primary_image': 'static/img/100x100.png'}];
	$scope.cart = {'total': '150', 'items': cart_items, 'shipping_fee': '0', 'total_tax': '0'};

	$scope.brands = [{'title': 'Apple', 'item_count': 50}, {'title': 'Orange', 'item_count': 50}, ]
}]);
