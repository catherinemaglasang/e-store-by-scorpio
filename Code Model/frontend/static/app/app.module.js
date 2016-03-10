// Primary Module
var mainApp = angular.module('MainApp', ['ngRoute']);

mainApp.config(['$routeProvider', function($routeProvider) {
	$routeProvider.
		when('/', {
			templateUrl: 'static/pages/shop/home.html',
		}).
		when('/page', {
			templateUrl: 'static/pages/shop/page.html',
		})
		.when('/blog/:id', {
			templateUrl: 'static/pages/shop/single_blog.html',
		})
		.when('/blog', {
			templateUrl: 'static/pages/shop/blog.html',
		}).
		when('/contact', {
			templateUrl: 'static/pages/shop/contact.html',
		}).
		when('/wishlist', {
			templateUrl: 'static/pages/shop/wishlist.html',
		}).
		when('/cart', {
			templateUrl: 'static/pages/shop/cart.html',
		}).
		when('/category/:id', {
			templateUrl: 'static/pages/shop/category.html'
		}).
		when('/category', {
			templateUrl: 'static/pages/shop/category.html'
		}).
		when('/product/:id', {
			templateUrl: 'static/pages/shop/product.html'
		}).
		when('/product', {
			templateUrl: 'static/pages/shop/product.html'
		}).
		when('/dashboard', {
			templateUrl: 'static/pages/shop/product.html'
		}).
		when('/account', {
			templateUrl: 'static/pages/shop/product.html'
		}).
		otherwise({
			templateUrl: 'static/pages/404.html'
		});
}]);

mainApp.controller("MainController", ['$scope','$http', function($scope,$http) {
	// Dummy Data
	$scope.products = [{'id': '1', 'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}]

	$scope.product = {'id': '1', 'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '#/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'};

	$scope.categories = [{'title': 'Tech', 'description': 'Tech Description', 'product_count': '152', 'primary_image': 'static/img/100x100.png'}, {'title': 'Home', 'description': 'Home Description', 'product_count': '100', 'primary_image': 'static/img/100x100.png'}];
	$scope.category_tree = [{'parent': 'Tech', 'children': [{'parent': 'Laptops', 'children': ['Mac', 'Ultra Books']}]}]

	$scope.tags = ['New Season', 'Watches', 'Classic'];
	$scope.promotions = [{'title': 'Save up to $150 on Your Next Laptop', 'description': 'I\'m Not Gonna Pay A Lot For This Laptop.', 'btn_link': '/#', 'btn_text': 'Shop Now', 'is_banner': 'true', 'primary_image': 'static/img/test_slider/1-i.png'}];

	$scope.store = [{'primary_logo': 'static/img/logo-w.png', 'name': 'TheStore', 'description': 'Store in a box'}];

	var cart_items = [{'price': '13', 'quantity': '1', 'title': 'Gucci Patent Leather Open Toe Platform', 'item_link': '#/', 'primary_image': 'static/img/100x100.png'}];
	$scope.cart = {'total': '150', 'items': cart_items, 'shipping_fee': '0', 'total_tax': '0'};

	$scope.brands = [{'title': 'Apple', 'item_count': 50}, {'title': 'Orange', 'item_count': 50}, ]

}]);

mainApp.directive("singleProduct", function(){
	return {
		restrict: 'E',
		templateUrl: "static/partials/single-product.html"
	};
});

mainApp.directive("cartItem", function(){
	return {
		restrict: 'E',
		templateUrl: "static/partials/cart-item.html"
	};
});

mainApp.directive("owlCarousel", function(){
	return {
		restrict: 'A',
		link: function(scope, element, attrs){
			$(element).owlCarousel(scope.$eval(attrs.owlCarousel));
		}
	}
});

mainApp.directive("priceSlider", function(){
	return {
		restrict: 'A',
		link: function(scope, element, attrs){
			$(element).ionRangeSlider(scope.$eval(attrs.priceSlider));
		}
	}
});

mainApp.directive("iCheck", function(){
	return {
		restrict: 'A',
		link: function(scope, element, attrs){
			$(element).iCheck({
				checkboxClass: 'i-check',
				radioClass: 'i-radio'
			});
		}
	}
})