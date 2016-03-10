// Primary Module
var mainApp = angular.module('mainApp', ['ngRoute']);

mainApp.config(['$routeProvider', function($routeProvider) {
	$routeProvider.
		when('/', {
			templateUrl: 'static/pages/shop/home.html',
		}).
		when('/category', {
			templateUrl: 'pages/shop/category.html'
		}).
		when('/category/:slug', {
			templateUrl: 'pages/shop/category.html'
		}).
		when('/product/:id', {
			templateUrl: 'pages/shop/product.html'
		}).
		otherwise({
			redirectTo: '/'
		});
}]);

mainApp.controller("HomeController", ['$scope','$http', function($scope,$http) {
	// Dummy Data
	$scope.products = [{'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '/#', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '/#', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': 'static/img/500x500.png', 'link_url': '/#', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}]
	$scope.categories = [{'title': 'Tech', 'description': 'Tech Description', 'product_count': '152', 'primary_image': 'static/img/100x100.png'}, {'title': 'Home', 'description': 'Home Description', 'product_count': '100', 'primary_image': 'static/img/100x100.png'}];
	$scope.tags = ['New Season', 'Watches', 'Classic'];
	$scope.promotions = [{'title': 'Save up to $150 on Your Next Laptop', 'description': 'I\'m Not Gonna Pay A Lot For This Laptop.', 'btn_link': '/#', 'btn_text': 'Shop Now', 'is_banner': 'true', 'primary_image': 'static/img/test_slider/1-i.png'}];

	// Activate home page carousel in controller. Note: Carousel won't work without this line.
	$('.owl-carousel').each(function(){
	  $(this).owlCarousel();
	});
}]);

mainApp.directive("singleProduct", function(){
	return {
		restrict: 'E',
		templateUrl: "static/partials/single-product.html"
	};
});