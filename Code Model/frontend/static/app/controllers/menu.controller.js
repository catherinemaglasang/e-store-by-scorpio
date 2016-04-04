mainApp.controller("MenuController", ['$scope', '$http', '$location', '$routeParams', function ($scope, $http, $location, $routeParams) {

    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };

}]);
