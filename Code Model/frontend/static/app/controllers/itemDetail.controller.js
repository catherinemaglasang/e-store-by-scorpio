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