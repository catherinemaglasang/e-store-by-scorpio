mainApp.controller('MainController', ['$scope', '$http', '$location', 'Item', 'Location', 'Supplier', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Location, Supplier, Attribute, $routeParams) {

    $scope.attribute = new Attribute();
    $scope.location = new Location();
    $scope.supplier = new Supplier();

    $scope.attributes = [];
    $scope.attribute_name = '';
    $scope.validation = '';

    $scope.itemList = [];
    $scope.attributeList = [];
    $scope.locationList = [];
    $scope.supplierList = [];

    $scope.addAttribute = function () {
        $scope.attribute.attribute_id = null;

        $scope.attribute.$save(function (data) {
            $scope.attribute = new Attribute();
            $location.path('/dashboard/attributes/all');
            $scope.initialize();
        });
    };

    $scope.addLocation = function () {
        $scope.location.location_id = null;
        $scope.location.$save(function () {
            $scope.location = new Location();
            $location.path('/dashboard/locations/all');
            $scope.initialize();
        });
    };

    $scope.addSupplier = function () {
        $scope.supplier.supplier_id = null;
        $scope.supplier.$save(function () {
            $scope.supplier = new Supplier();
            $location.path('/dashboard/suppliers/all');
            $scope.initialize();
        });
    };


    $scope.initialize = function () {
        Item.get(function (data) {
            $scope.itemList = data.entries;
        });

        Attribute.get(function (data) {
            $scope.attributeList = data.entries;
        });

        Location.get(function (data) {
            $scope.locationList = data.entries;
        });
        Supplier.get(function (data) {
            $scope.supplierList = data.entries;
        });
    };

    $scope.initialize();
}]);



mainApp.controller('LocationDetailController', ['$scope', '$http', '$location', 'Item', 'Location', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Location, Attribute, $routeParams) {
    var locationId = $routeParams.id;

    $scope.location = '';

    $scope.getLocationDetail = function () {
        Location.get({id: locationId}, function (data) {
            $scope.location = data.entries[0];
        });
    };

    $scope.updateLocationDetail = function () {
        Location.update({id: locationId}, $scope.location, function () {
            $location.path('/dashboard/locations/all');
        });
    };

    $scope.getLocationDetail();
}]);

mainApp.controller('AttributeDetailController', ['$scope', '$http', '$location', 'Attribute', '$routeParams', function ($scope, $http, $location, Attribute, $routeParams) {
    var attributeId = $routeParams.id;

    $scope.attribute = {};

    $scope.getAttributeDetail = function () {
        Attribute.get({id: attributeId}, function (data) {
            $scope.attribute = data.entries[0];
            console.log($scope.attribute);
        });
    };

    $scope.updateAttributeDetail = function () {
        Attribute.update({id: attributeId}, $scope.attribute, function (data) {
            $location.path('/dashboard/attributes/all');
        });
    };

    $scope.getAttributeDetail();
}]);




