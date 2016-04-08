
mainApp.controller('OptionCtrl', ['$scope', '$http', '$location', 'Option', 'OptionGroup', '$routeParams', function ($scope, $http, $location, Option, OptionGroup, $routeParams) {
    $scope.optionGroupList = [];

    var getOptionList = function(gid){
        Option.get({optiongroupid: gid}, function(data){
            console.log(data.entries);
            return data.entries;
        });
    };

    $scope.initialize = function () {
        OptionGroup.get(function (data) {
            $scope.optionGroupList = data.entries;

            angular.forEach($scope.optionGroupList, function(value, key){
                value.optionList = getOptionList(value.option_group_id);
            });
        });
    };

    $scope.initialize();
}]);