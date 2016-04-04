mainApp.config(function ($routeProvider, $locationProvider, $resourceProvider) {

    $routeProvider
        .when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'MainController'
        })

        .when('/reports', {
            templateUrl: 'pages/reports.html',
            controller: 'MainController'
        })

        // Inventory Module

        .when('/inventory/items/all', {
            templateUrl: 'pages/inventory/item_list.html',
            controller: 'MainController'
        })


        .when('/inventory/types/all', {
            templateUrl: 'pages/inventory/type_list.html',
            controller: 'MainController'
        })


        .when('/inventory/locations/all', {
            templateUrl: 'pages/inventory/location_list.html',
            controller: 'MainController'
        })

        .when('/inventory/items/add', {
            templateUrl: 'pages/inventory/item_form.html',
            controller: 'MainController'
        })

        .when('/inventory/types/add', {
            templateUrl: 'pages/inventory/type_form.html',
            controller: 'MainController'
        })

        .when('/inventory/locations/add', {
            templateUrl: 'pages/inventory/location_form.html',
            controller: 'MainController'
        })

        .when('/inventory', {
            templateUrl: 'pages/inventory/inventory.html',
            controller: 'MainController'
        })

        .when('/inventory/items/:id', {
            templateUrl: 'pages/inventory/item_detail.html',
            controller: 'MainController'
        })

        .when('/inventory/types/:id', {
            templateUrl: 'pages/inventory/type_detail.html',
            controller: 'TypeDetailController'
        })

        .when('/inventory/locations/:id', {
            templateUrl: 'pages/inventory/location_detail.html',
            controller: 'MainController'
        })

        // Supply & Purchasing Module

        .when('/purchase', {
            templateUrl: 'pages/purchase.html',
            controller: 'MainController'
        })

        .when('/purchase/add', {
            templateUrl: 'pages/purchase_add.html',
            controller: 'MainController'
        })

        .when('/vendors/add', {
            templateUrl: 'pages/purchase_add.html',
            controller: 'MainController'
        })

        // Point of Sales Module

        .when('/sales', {
            templateUrl: 'pages/sales.html',
            controller: 'MainController'
        })

        .when('/sales/add', {
            templateUrl: 'pages/sales_add.html',
            controller: 'MainController'
        })

        // Stock movement and transfer Module

        .when('/adjustment', {
            templateUrl: 'pages/adjustment.html',
            controller: 'MainController'
        })

        .when('/adjustment/add', {
            templateUrl: 'pages/adjustment_add.html',
            controller: 'MainController'
        })

        .when('/transfer', {
            templateUrl: 'pages/transfer.html',
            controller: 'MainController'
        })

        .when('/transfer/add', {
            templateUrl: 'pages/transfer_add.html',
            controller: 'MainController'
        })

        // Dashboard Pages

        .when('/dashboard/suppliers/add', {
            templateUrl: 'pages/dashboard/suppliers/add_supplier.html',
            controller: 'MainController'
        })

        .when('/dashboard/suppliers/all', {
            templateUrl: 'pages/dashboard/suppliers/suppliers.html',
            controller: 'MainController'
        })

        // 404 Pages

        .when('/404', {
            templateUrl: 'pages/404.html'
        })

        .otherwise({
            redirectTo: '/inventory/items/all'
        });

    $resourceProvider.defaults.stripTrailingSlashes = false;
});
