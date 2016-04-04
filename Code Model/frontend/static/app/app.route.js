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
            templateUrl: 'pages/dashboard/inventory/item_list.html',
            controller: 'MainController'
        })


        .when('/inventory/types/all', {
            templateUrl: 'pages/dashboard/inventory/type_list.html',
            controller: 'MainController'
        })


        .when('/inventory/locations/all', {
            templateUrl: 'pages/dashboard/inventory/location_list.html',
            controller: 'MainController'
        })

        .when('/inventory/items/add', {
            templateUrl: 'pages/dashboard/inventory/item_form.html',
            controller: 'MainController'
        })

        .when('/inventory/types/add', {
            templateUrl: 'pages/dashboard/inventory/type_form.html',
            controller: 'MainController'
        })

        .when('/inventory/locations/add', {
            templateUrl: 'pages/dashboard/inventory/location_form.html',
            controller: 'MainController'
        })

        .when('/inventory', {
            templateUrl: 'pages/dashboard/inventory/inventory.html',
            controller: 'MainController'
        })

        .when('/inventory/items/:id', {
            templateUrl: 'pages/dashboard/inventory/item_detail.html',
            controller: 'MainController'
        })

        .when('/inventory/types/:id', {
            templateUrl: 'pages/dashboard/inventory/type_detail.html',
            controller: 'TypeDetailController'
        })

        .when('/inventory/locations/:id', {
            templateUrl: 'pages/dashboard/inventory/location_detail.html',
            controller: 'MainController'
        })

        // Supply & Purchasing Module

        .when('/purchase', {
            templateUrl: 'pages/dashboard/inventory/purchase.html',
            controller: 'MainController'
        })

        .when('/purchase/add', {
            templateUrl: 'pages/dashboard/inventory/purchase_add.html',
            controller: 'MainController'
        })

        .when('/vendors/add', {
            templateUrl: 'pages/dashboard/inventory/purchase_add.html',
            controller: 'MainController'
        })

        // Point of Sales Module

        .when('/sales', {
            templateUrl: 'pages/dashboard/inventory/sales.html',
            controller: 'MainController'
        })

        .when('/sales/add', {
            templateUrl: 'pages/dashboard/inventory/sales_add.html',
            controller: 'MainController'
        })

        // Stock movement and transfer Module

        .when('/adjustment', {
            templateUrl: 'pages/dashboard/inventory/adjustment.html',
            controller: 'MainController'
        })

        .when('/adjustment/add', {
            templateUrl: 'pages/dashboard/inventory/adjustment_add.html',
            controller: 'MainController'
        })

        .when('/transfer', {
            templateUrl: 'pages/dashboard/inventory/transfer.html',
            controller: 'MainController'
        })

        .when('/transfer/add', {
            templateUrl: 'pages/dashboard/inventory/transfer_add.html',
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
