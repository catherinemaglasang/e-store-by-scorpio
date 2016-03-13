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
			templateUrl: 'static/pages/dashboard/home.html',
            controller: 'DashboardController'
		}).
		when('/dashboard/products', {
			templateUrl: 'static/pages/dashboard/products/products.html',
            controller: 'DashboardController',
		}).
		when('/dashboard/products/add', {
			templateUrl: 'static/pages/dashboard/products/add_product.html',
            controller: 'DashboardController'
		}).
		when('/account', {
			templateUrl: 'static/pages/account/home.html'
		}).
		otherwise({
			templateUrl: 'static/pages/404.html'
		});
}]);