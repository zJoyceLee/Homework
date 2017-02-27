var app = angular.module('todoList', []);
app.controller('myCtrl', function($scope) {
  $scope.todo = "";
  $scope.todos = [];
  $scope.add = function(){
    $scope.todos.push($scope.todo);	
  };
});