mainApp.config(function ($routeProvider, $locationProvider, $resourceProvider) {

    $routeProvider
    // Authentication Module

        .when('/login', {
            templateUrl: 'pages/user/login.html',
            controller: 'MainController'
        })

        // Reports & Analytics Module

        .when('/reports', {
            templateUrl: 'pages/reports/reports.html',
            controller: 'MainController'
        })

        // Inventory Module

        .when('/dashboard/items/all', {
            templateUrl: 'pages/dashboard/items/item_list.html',
            controller: 'MainController'
        })


        .when('/dashboard/types/all', {
            templateUrl: 'pages/dashboard/items/type_list.html',
            controller: 'MainController'
        })


        .when('/dashboard/locations/all', {
            templateUrl: 'pages/dashboard/items/location_list.html',
            controller: 'MainController'
        })

        .when('/dashboard/items/add', {
            templateUrl: 'pages/dashboard/items/item_form.html',
            controller: 'MainController'
        })

        .when('/dashboard/types/add', {
            templateUrl: 'pages/dashboard/items/type_form.html',
            controller: 'MainController'
        })

        .when('/dashboard/locations/add', {
            templateUrl: 'pages/dashboard/items/location_form.html',
            controller: 'MainController'
        })

        .when('/dashboard', {
            templateUrl: 'pages/dashboard/items/home.html',
            controller: 'MainController'
        })

        .when('/dashboard/items/:id', {
            templateUrl: 'pages/dashboard/items/item_detail.html',
            controller: 'ItemDetailController'
        })

        .when('/dashboard/types/:id', {
            templateUrl: 'pages/dashboard/items/type_detail.html',
            controller: 'TypeDetailController'
        })

        .when('/dashboard/locations/:id', {
            templateUrl: 'pages/dashboard/items/location_detail.html',
            controller: 'LocationDetailController'
        })

        .when('/dashboard/purchase/all', {
            templateUrl: 'pages/dashboard/items/purchase.html',
            controller: 'MainController'
        })

        .when('/dashboard/purchase/add', {
            templateUrl: 'pages/dashboard/items/purchase_add.html',
            controller: 'MainController'
        })

        // Stock movement and transfer Module

        .when('/dashboard/adjustment/all', {
            templateUrl: 'pages/dashboard/items/adjustment.html',
            controller: 'MainController'
        })

        .when('/dashboard/adjustment/add', {
            templateUrl: 'pages/dashboard/items/adjustment_add.html',
            controller: 'MainController'
        })

        .when('/dashboard/transfer/all', {
            templateUrl: 'pages/dashboard/items/transfer.html',
            controller: 'MainController'
        })

        .when('/dashboard/transfer/add', {
            templateUrl: 'pages/dashboard/items/transfer_add.html',
            controller: 'MainController'
        })

        .when('/dashboard/suppliers/add', {
            templateUrl: 'pages/dashboard/suppliers/add_supplier.html',
            controller: 'MainController'
        })

        .when('/dashboard/suppliers/all', {
            templateUrl: 'pages/dashboard/suppliers/suppliers.html',
            controller: 'MainController'
        })

        // Point of Sales & Cart Module

        .when('/sales', {
            templateUrl: 'pages/dashboard/items/sales.html',
            controller: 'MainController'
        })

        .when('/sales/add', {
            templateUrl: 'pages/dashboard/items/sales_add.html',
            controller: 'MainController'
        })

        // 404 Pages

        .when('/404', {
            templateUrl: 'pages/404.html'
        })

        .otherwise({
            redirectTo: '/dashboard/items/all'
        });

    $resourceProvider.defaults.stripTrailingSlashes = false;
});
