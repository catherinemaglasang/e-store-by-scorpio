mainApp.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/shop/');
	$stateProvider
		.state('dashboard', {
			url: '/dashboard',
			templateUrl: 'static/pages/dashboard/base.html'
		})
		.state('dashboard.home', {
			url: '/',
			templateUrl: 'static/pages/dashboard/home.html'
		})
		.state('dashboard.products', {
			url: '/products',
			templateUrl: 'static/pages/dashboard/products/products.html'
		})
		.state('dashboard.add_product', {
			url: '/products/add',
			templateUrl: 'static/pages/dashboard/products/add_product.html'
		})

		.state('shop', {
			url: '/shop',
			templateUrl: 'static/pages/shop/base.html'
		})
		.state('shop.home', {
			url: '/',
			templateUrl: 'static/pages/shop/home.html'
		})
		.state('shop.page', {
			url: '/page',
			templateUrl: 'static/pages/shop/page.html'
		})
		.state('shop.blog', {
			url: '/blog',
			templateUrl: 'static/pages/shop/blog.html'
		})
		.state('shop.contact', {
			templateUrl: 'static/pages/shop/contact.html'
		})
		.state('shop.wishlist', {
			url: '/wishlist',
			templateUrl: 'static/pages/shop/wishlist.html'
		})
		.state('shop.cart', {
			url: '/cart',
			templateUrl: 'static/pages/shop/cart.html'
		})
		.state('shop.category', {
			url: '/category',
			templateUrl: 'static/pages/shop/category.html'
		})
		.state('shop.product', {
			url: '/product',
			templateUrl: 'static/pages/shop/product.html'
		})
		.state('login', {
			url: '/login',
			templateUrl: 'static/pages/login.html'
		})
		.state('register', {
			url: '/register',
			templateUrl: 'static/pages/register.html'
		})
		.state('password_reset', {
			url: '/password/reset',
			templateUrl: 'static/pages/password_reset.html'
		});
}]);