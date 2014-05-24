var app = angular.module('PizzaApp', ['ui.router', 'ng.django.forms']);

app.config(function ($httpProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.config(function ($stateProvider, $urlRouterProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('index', {

            url: "/",
            templateUrl: "/static/html/partials/_job_list.html",
            controller: "JobList"
        })

       .state('new', {

            url: "/new",
            templateUrl: "/jobs/job-form",
            controller: "JobFormCtrl"
        })
})

