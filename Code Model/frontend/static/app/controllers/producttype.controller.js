mainApp.controller("ProductTypeController", ['$scope', '$http', '$location', 'ApiService', '$routeParams', function ($scope, $http, $location, ApiService, $routeParams) {
    // Local variables
    var productTypeApi = ApiService.ProductType;
    var productTypeId = $routeParams.id;

    // Global variables
    $scope.productTypeList = [];
    $scope.postData = new productTypeApi();

    // Functions
    $scope.getProductType = function () {
        productTypeApi.query(function (data) {
            $scope.productTypeList = data.entries;
        });
    };

    $scope.getProductTypeById = function(id){
        productTypeApi.query({id: id}, function (data) {
            var single = data.entries;
            console.log(single);
        });
    };

    $scope.updateProductType = function(id){
        console.log("clicked");
        console.log(id);
        //$scope.productType.update(function(data){
        //    $location.path('/types')
        //});
    };

    $scope.addProductType = function(){
        $scope.postData.$save(function(){
            $scope.postData = new productTypeApi();
            $location.path('/types')
        });
    };

    $scope.deleteProductType = function(){

    };

    // Initialize
    $scope.getProductType();
    $scope.productType = $scope.getProductTypeById(productTypeId);
    console.log($scope.productType);

}]);
