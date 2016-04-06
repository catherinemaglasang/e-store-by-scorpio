mainApp.config(function ($routeProvider, $locationProvider, $resourceProvider) {

    $routeProvider
    // Authentication Module

        .when('/login', {
            templateUrl: 'pages/user/login.html',
            controller: 'MainController'
        })

        .when('/dashboard/settings', {
            templateUrl: 'pages/dashboard/settings.html',
            controller: 'MainController'
        })

        // Reports & Analytics Module

        .when('/dashboard/reports', {
            templateUrl: 'pages/dashboard/reports/reports.html',
            controller: 'MainController'
        })

        // Inventory Module
        .when('/dashboard', {
            templateUrl: 'pages/dashboard/home.html',
            controller: 'MainController'
        })

        .when('/dashboard/items/all', {
            templateUrl: 'pages/dashboard/items/item_list.html',
            controller: 'MainController'
        })


        .when('/dashboard/attributes/all', {
            templateUrl: 'pages/dashboard/items/attribute_list.html',
            controller: 'MainController'
        })


        .when('/dashboard/locations/all', {
            templateUrl: 'pages/dashboard/items/location_list.html',
            controller: 'MainController'
        })

        .when('/dashboard/items/add', {
            templateUrl: 'pages/dashboard/items/item_form.html',
            controller: 'ItemAddController'
        })

        .when('/dashboard/attributes/add', {
            templateUrl: 'pages/dashboard/items/attribute_form.html',
            controller: 'MainController'
        })

        .when('/dashboard/locations/add', {
            templateUrl: 'pages/dashboard/items/location_form.html',
            controller: 'MainController'
        })

        .when('/dashboard/items/:id', {
            templateUrl: 'pages/dashboard/items/item_detail.html',
            controller: 'ItemDetailController'
        })

        .when('/dashboard/attributes/:id', {
            templateUrl: 'pages/dashboard/items/attribute_detail.html',
            controller: 'AttributeDetailController'
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

        .when('/dashboard/sales/all', {
            templateUrl: 'pages/dashboard/items/sales.html',
            controller: 'MainController'
        })

        .when('/dashboard/sales/add', {
            templateUrl: 'pages/dashboard/items/sales_add.html',
            controller: 'MainController'
        })

        // 404 Pages

        .when('/404', {
            templateUrl: 'pages/404.html'
        })

        .otherwise({
            redirectTo: '/dashboard'
        });

    $resourceProvider.defaults.stripTrailingSlashes = false;
});
