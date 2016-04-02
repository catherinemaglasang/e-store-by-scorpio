mainApp.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/shop/');
	$stateProvider
		.state('dashboard', {
			url: '/dashboard',
			templateUrl: 'static/pages/dashboard/base.html',
			controller: 'DashboardController'
		})
		.state('dashboard.home', {
			url: '/',
			templateUrl: 'static/pages/dashboard/home.html',
			controller: 'DashboardController'
		})
		.state('dashboard.items', {
			url: '/items',
			templateUrl: 'static/pages/dashboard/products/products.html',
			controller: 'DashboardController'
		})
		.state('dashboard.add_product', {
			url: '/items/add',
			templateUrl: 'static/pages/dashboard/products/add_product.html',
			controller: 'DashboardController'
		})

		.state('shop', {
			url: '/shop',
			templateUrl: 'static/pages/shop/base.html',
			controller: 'ShopController'
		})
		.state('shop.home', {
			url: '/',
			templateUrl: 'static/pages/shop/home.html'
		})
		.state('shop.page', {
			url: '/page',
			templateUrl: 'static/pages/shop/simple/page.html'
		})
		.state('shop.blog', {
			url: '/blog',
			templateUrl: 'static/pages/shop/blog/blog.html'
		})
		.state('shop.contact', {
			templateUrl: 'static/pages/shop/simple/contact.html'
		})
		.state('shop.cart', {
			url: '/cart',
			templateUrl: 'static/pages/shop/checkout/cart.html'
		})
		.state('shop.checkout', {
			url: '/checkout',
			templateUrl: 'static/pages/shop/checkout/checkout.html'
		})
		.state('shop.catalogue', {
			url: '/catalogue',
			templateUrl: 'static/pages/shop/product/category.html'
		})
		.state('shop.categoryDetail', {
			url: '/category/:id',
			templateUrl: 'static/pages/shop/product/category.html'
		})
		.state('shop.productDetail', {
			url: '/product/:id',
			templateUrl: 'static/pages/shop/product.html'
		})
		.state('shop.login', {
			url: '/login',
			templateUrl: 'static/pages/login.html'
		})
		.state('shop.register', {
			url: '/register',
			templateUrl: 'static/pages/register.html'
		})
		.state('shop.password_reset', {
			url: '/password/reset',
			templateUrl: 'static/pages/password_reset.html'
		})
		.state('shop.account', {
			url: '/account',
			templateUrl: 'static/pages/account/base.html'
		})
		.state('shop.account.home', {
			url: '/',
			templateUrl: 'static/pages/account/profile.html'
		})
		.state('shop.account.orders', {
			url: '/orders',
			templateUrl: 'static/pages/account/orders.html'
		}).state('shop.account.address', {
			url: '/address',
			templateUrl: 'static/pages/account/address_book.html'
		}).state('shop.account.notifications', {
			url: '/notifications',
			templateUrl: 'static/pages/account/notifications.html'
		}).state('shop.account.wishlist', {
			url: '/wishlist',
			templateUrl: 'static/pages/account/wishlist.html'
		});
}]);