mainApp.controller('MainController', ['$scope', '$http', '$location', 'Item', 'Type', 'Location', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Type, Location, Attribute, $routeParams) {
    $scope.item = new Item();
    $scope.location = new Location();
    $scope.type = new Type();

    $scope.attributes = [];
    $scope.attribute_name = '';
    $scope.validation = '';

    $scope.itemList = [];
    $scope.typeList = [];
    $scope.attributeList = [];
    $scope.locationList = [];

    $scope.typeDetail = [];

    $scope.getItemList = function () {
        Item.get(function (data) {
            $scope.itemList = data.entries;
        });

        Type.get(function (data) {
            $scope.typeList = data.entries;
        });

        Location.get(function (data) {
            $scope.locationList = data.entries;
        });
    };

    //items_upsert(NULL, NULL, 'SN153', NULL, NULL, 'Apple', 'test desc', NULL, NULL, TRUE, 10.01, TRUE, TRUE);

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

    $scope.addType = function () {
        $scope.type.type_id = null;

        angular.forEach($scope.typeList, function (values, key) {
            $scope.attributeList.push(values.type_id)
        });

        $scope.type.$save(function (data) {
            var id = data.entries[0].types_upsert;
            angular.forEach($scope.attributes, function (values, key) {
                // Now we save each attributes for each type
                values.type_id = id;
                values.attribute_id = null;
                values.$save({typeid: id}, function (data) {
                    console.log("Added Attribute for type: " + id);
                })
            });

            $scope.attributes = [];
            $scope.type = new Type();
            $location.path('/dashboard/types/all');
            $scope.initialize();
        });
    };

    $scope.addAttribute = function () {
        $scope.attributes.push(new Attribute({
            'attribute_name': $scope.attribute_name,
            'validation': $scope.validation
        }));
        $scope.attribute_name = '';
        $scope.validation = '';
        console.log($scope.attributes);
    };

    $scope.addLocation = function () {
        $scope.location.location_id = null;
        $scope.location.$save(function () {
            $scope.location = new Location();
            $location.path('/dashboard/locations/all');
            $scope.initialize();
        });
    };

    $scope.updateItem = function () {

    };

    $scope.deleteItem = function () {

    };

    $scope.initialize = function () {
        $scope.getItemList();
    };

    $scope.initialize();
}]);

mainApp.controller('ItemDetailController', ['$scope', '$http', '$location', 'Item', 'Type', 'Location', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Type, Location, Attribute, $routeParams) {
    var itemId = $routeParams.id;

    $scope.item = '';

    $scope.getItemDetail = function () {
        Item.get({id: itemId}, function (data) {
            $scope.item = data.entries[0];
        });
    };

    $scope.updateItemDetail = function () {
        Item.update({ id: itemId }, $scope.type, function(){
            $location.path('/dashboard/items/all');
        });
    };

    $scope.getItemDetail();
}]);

mainApp.controller('TypeDetailController', ['$scope', '$http', '$location', 'Item', 'Type', 'Location', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Type, Location, Attribute, $routeParams) {
    var typeId = $routeParams.id;

    $scope.type = '';

    $scope.getTypeDetail = function () {
        Type.get({id: typeId}, function (data) {
            $scope.type = data.entries[0];
            console.log($scope.type);
        });
    };

    $scope.updateTypeDetail = function () {
        Type.update({ id: typeId }, $scope.type, function(){
            $location.path('/dashboard/types/all');
        });
    };

    $scope.getTypeDetail();
}]);

mainApp.controller('LocationDetailController', ['$scope', '$http', '$location', 'Item', 'Type', 'Location', 'Attribute', '$routeParams', function ($scope, $http, $location, Item, Type, Location, Attribute, $routeParams) {
    var locationId = $routeParams.id;

    $scope.location = '';

    $scope.getLocationDetail = function () {
        Location.get({id: locationId}, function (data) {
            $scope.location = data.entries[0];
        });
    };

    $scope.updateLocationDetail = function () {
        Location.update({ id: locationId }, $scope.location, function(){
            $location.path('/dashboard/locations/all');
        });
    };

    $scope.getLocationDetail();
}]);



