mainApp.controller('ItemAddController', ['$scope', '$http', '$location', 'Item', 'Location', 'Attribute', 'ItemAttribute', 'OptionGroup', 'Option', 'ItemVariation', '$routeParams', '$filter', function ($scope, $http, $location, Item, Location, Attribute, ItemAttribute, OptionGroup, Option, ItemVariation, $routeParams, $filter) {
    // -------------------------
    // Primary Instance
    // -------------------------
    $scope.item = new Item();
    ////////////////////////////

    $scope.attributeList = [];
    $scope.optionGroupList = [];
    $scope.optionList = [];

    $scope.attribute = new ItemAttribute();
    $scope.image = new Image();

    $scope.itemVariations = [];
    $scope.itemAttributes = [];
    $scope.images = [];

    /**
     * Add Item Function
     * Workflow includes saving the item -> item_attributes -> item_variations -> images
     */
    $scope.addItem = function () {
        $scope.item.item_id = null;

        // http://www.angulartutorial.net/2014/04/date-filtering-and-formatting-in.html
        $scope.item.date_added = $filter('date')(Date.now(), 'MMM-dd-yyyy HH:mm:ss');
        $scope.item.date_updated = $filter('date')(Date.now(), 'MMM-dd-yyyy HH:mm:ss');

        $scope.item.is_active = true;
        $scope.item.has_variations = true;

        /////////////////

        $scope.item.$save(function (data) {
            var id = data.entries[0].items_upsert;

            //////////////

            angular.forEach($scope.itemAttributes, function (value, key) {
                value.item_id = id;
                value.$save({itemid: id}, function (data) {
                    console.log("Added item_attribute " + value);
                });
            });

            //////////////

            angular.forEach($scope.itemVariations, function (value, key) {
                value.item_id = id;
                value.$save({itemid: id}, function (data) {
                    console.log("Added item_variation " + value);
                });
            });

            //////////////

            $scope.item = new Item();
            $location.path('/dashboard/items/all');
            $scope.initialize();
        });
    };

    /*
     * Add Item Attribute
     * Triggered in the client. Pushes the new item_attribute instance in array.
     */
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