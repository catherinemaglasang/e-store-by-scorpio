mainApp.controller('MainController', ['$scope', '$http', '$location', 'Item', 'Location', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Location, Attribute, $routeParams) {

    $scope.attribute = new Attribute();
    $scope.location = new Location();

    $scope.itemList = [];
    $scope.typeList = [];
    $scope.attributeList = [];
    $scope.locationList = [];

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
    };

    $scope.initialize();
}]);

mainApp.controller('ItemDetailController', ['$scope', '$http', '$location', 'Item', 'Location', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Location, Attribute, $routeParams) {
    var itemId = $routeParams.id;

    $scope.item = '';

    $scope.getItemDetail = function () {
        Item.get({id: itemId}, function (data) {
            $scope.item = data.entries[0];
        });
    };

    $scope.updateItemDetail = function () {
        Item.update({id: itemId}, $scope.item, function () {
            $location.path('/dashboard/items/all');
        });
    };

    $scope.getItemDetail();
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

mainApp.controller('ItemAddController', ['$scope', '$http', '$location', 'Item', 'Location', 'Attribute', 'ItemAttribute', '$routeParams', function ($scope, $http, $location, Item, Location, Attribute, ItemAttribute, $routeParams) {
    $scope.attributeList = [];

    $scope.item = new Item();
    $scope.options = [];
    $scope.optionGroups = [];
    $scope.itemVariationOptions = [];
    $scope.itemAttributes = [];

    $scope.attribute_id = '';
    $scope.attribute_value = '';

    $scope.addItem = function () {
        $scope.item.item_id = null;
        $scope.item.site_id = null;
        //$scope.item.serial_no = 'SN1';
        $scope.item.tax_class_id = null;
        //$scope.item.type_id = null;
        $scope.item.name = 'name';
        $scope.item.description = 'name';
        $scope.item.date_added = null;
        $scope.item.date_updated = null;
        $scope.item.is_taxable = true;
        $scope.item.unit_cost = null;
        $scope.item.is_active = true;
        $scope.item.has_variations = true;

        $scope.item.$save(function (data) {
            var id = data.entries[0].items_upsert;
            console.log(id);

            $scope.item = new Item();
            $location.path('/dashboard/items/all');
            $scope.initialize();
        });
    };

    $scope.addItemAttribute = function () {
        $scope.itemAttributes.push(new ItemAttribute({
            'attribute_id': $scope.attribute_id,
            'attribute_value': $scope.attribute_value
        }));
        $scope.attribute_id = '';
        $scope.attribute_value = '';
        console.log($scope.itemAttributes);
    };

    $scope.initialize = function () {
        Attribute.get(function (data) {
            $scope.attributeList = data.entries;
        });
    };

    $scope.initialize();

}]);




