var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'static/partials/home.html',
    })
    .when('/dashboard', {
      templateUrl: 'static/partials/dashboard.html',
    })
    .when('/dashboard/product', {
      templateUrl: 'static/partials/dashboard.html',
      controller: 'ProductController'
    })
    .otherwise({redirectTo: '/'});
});
