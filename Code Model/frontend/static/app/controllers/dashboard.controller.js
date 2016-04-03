mainApp.controller("DashboardController", ['$scope', '$http', 'Product', function ($scope, $http, Product) {
    // Dummy Data
    $scope.productList = [];

    $scope.getProductList = function () {
        Product.get(function (data) {
            $scope.productList = data.entries;
            console.log($scope.productList);

        });
    };

    $scope.initialize = function () {
        $scope.getProductList();
    };

    $scope.initialize();


}]);
