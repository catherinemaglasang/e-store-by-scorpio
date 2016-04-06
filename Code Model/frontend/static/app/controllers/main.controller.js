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

mainApp.controller('ItemAddController', ['$scope', '$http', '$location', 'Item', 'Location', 'Attribute', 'ItemAttribute', 'OptionGroup', 'Option', 'ItemVariation', '$routeParams', function ($scope, $http, $location, Item, Location, Attribute, ItemAttribute, OptionGroup, Option, ItemVariation, $routeParams) {
    // Form dropdowns
    $scope.attributeList = [];
    $scope.optionGroupList = [];
    $scope.optionList = [];

    // Item instance
    $scope.item = new Item();
    $scope.attribute = new Attribute();

    // To be saved after item
    $scope.itemVariations = [];
    $scope.itemAttributes = [];
    $scope.images = [];

    $scope.attribute_value = 'hi';
    $scope.attribute_id = 'hi';
    $scope.group_id = 0;

    $scope.addItem = function () {
        $scope.item.item_id = null;

        $scope.item.$save(function (data) {
            var id = data.entries[0].items_upsert;
            console.log(id);

            $scope.item = new Item();
            $location.path('/dashboard/items/all');
            $scope.initialize();
        });
    };

    $scope.addItemAttribute = function () {
        $scope.itemAttributes.push($scope.attribute);
        $scope.attribute = new Attribute();
    };

    $scope.removeItemAttribute = function (attr) {
        var index = $scope.itemAttributes.indexOf(attr);
        $scope.itemAttributes.splice(index, 1);
    };

    $scope.updateItemAttribute = function (attr) {
        var index = $scope.itemAttributes.indexOf(attr);
        $scope.itemAttributes.splice(index, 1, $scope.attribute);
    };

    $scope.populateOptionGroup = function (gid) {
        $scope.group_id = gid;
        Option.get({optiongroupid: gid}, function (data) {
            $scope.optionList = data.entries;
            $scope.populateItemVariation();
        });
    };

    $scope.populateItemVariation = function () {
        $scope.itemVariations = [];
        angular.forEach($scope.optionList, function (value, key) {
            var variant = new ItemVariation();
            variant.option_id = value.option_id;
            variant.option_group_id = value.option_group_id;
            variant.option_value = value.option_value;
            variant.is_active = true;
            variant.editable = true;
            $scope.itemVariations.push(variant);
            console.log($scope.itemVariations);
        });
    };

    $scope.updateItemVariation = function (variant) {
        variant.editable = false;
        var index = $scope.itemVariations.indexOf(variant);
        $scope.itemVariations.splice(index, 1, variant);
        console.log($scope.itemVariations);
    };

    $scope.make_editable = function (variant) {
        variant.editable = true;
        var index = $scope.itemVariations.indexOf(variant);
        $scope.itemVariations.splice(index, 1, variant);
    };

    $scope.initialize = function () {
        Attribute.get(function (data) {
            $scope.attributeList = data.entries;
        });

        OptionGroup.get(function (data) {
            $scope.optionGroupList = data.entries;
        });
    };

    $scope.initialize();

}]);




