mainApp.factory("Product", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/products/:id/", {id: '@id'}, {});
    }]);
