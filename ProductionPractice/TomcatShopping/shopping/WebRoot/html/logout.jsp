<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 5 Transitional//EN">
<html>
	<head>
		<base href="<%=basePath%>">		
		<title>退出登录</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8"> 
		<meta http-equiv="pragma" content="no-cache">
		<meta http-equiv="cache-control" content="no-cache">
		<meta http-equiv="expires" content="0">    
		<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
		<meta http-equiv="description" content="This is my page">
	
	</head>
	
	<body>
		<%
			request.setCharacterEncoding("utf-8");
			response.setCharacterEncoding("utf-8");
		%>
		<%
			session.invalidate();
			response.sendRedirect("http://localhost:8080/shopping/html/index.jsp");
		%>
	</body>
</html>
