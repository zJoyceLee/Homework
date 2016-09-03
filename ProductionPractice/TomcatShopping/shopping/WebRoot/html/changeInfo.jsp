<!DOCTYPE html >
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<jsp>
<head>
<title>会员信息</title>
<!--mobile apps-->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Liqueur Responsive web template, Bootstrap Web Templates, Flat Web Templates, Android Compatible web template, 
	Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyEricsson, Motorola web design" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!--mobile apps-->
<!--Custom Theme files -->
<link href="css/bootstrap.css" type="text/css" rel="stylesheet" media="all">
<link href="css/style.css" type="text/css" rel="stylesheet" media="all">
<!-- //Custom Theme files -->
<!-- js -->
<script src="js/jquery-1.11.1.min.js"></script> 
<!-- //js -->


<%@ page language="java" import="javaBean.User"%>

<style type="text/css">
body {padding: 150px;}
</style>

</head>
<body>
<%
			request.setCharacterEncoding("utf-8");
			response.setCharacterEncoding("utf-8");
%>
<%		User user = (User) session.getAttribute("user");
			if (user == null) {
				response.sendRedirect("index.jsp");
				return;
			}
%>
	<div class="blog-left1 wow fadeInDownBig animated" data-wow-delay=".5s">
		<h3 class="title wow fadeInLeftBig animated" data-wow-delay=".5s">个人信息：</h3>			
		<div class="contact-form">
			<form action="http://localhost:8080/shopping/servlet/changeServlet" method="post">
				<table class="table table-striped" width="100">
			
						<tbody>
							<tr>
								
								<td>&nbsp;</td>
								<td>&nbsp;</td>	
								<td>&nbsp;</td>		
								<td><h1>用户名：</h1></td>
								<td><h1><%=user.getUsername()%></h1></td>
								<td>&nbsp;</td>	
												
					</tr>
					
					<tr>
								
								<td>&nbsp;</td>
								<td>&nbsp;</td>	
								<td>&nbsp;</td>
								<td><h1>电&nbsp;话：</h1></td>
								<td><h4><input name="phone" type="text" size="50"/></h4></td>
								<td>&nbsp;</td>
								
					</tr>
					<tr>
								
								<td>&nbsp;</td>
								<td>&nbsp;</td>
								<td>&nbsp;</td>	
								<td><h1>地&nbsp;址：</h1></td>
								<td><h4><input name="addr" type="text"size="50"/></h4></td>
								<td>&nbsp;</td>
								
					</tr>
					<tr>
								<td>&nbsp;</td>
								<td>&nbsp;</td>
								<td>&nbsp;</td>
								<td><h1>邮&nbsp;箱：</h1></td>
								<td><h4><input name="email" type="text" size="50"/></h4></td>
								<td>&nbsp;</td>
								
					</tr>
					<tr>
					
								<td>&nbsp;</td>
								<td>&nbsp;</td>
								<td>&nbsp;</td>
								<td>&nbsp;</td>
								<td>&nbsp;</td>	
								<td><h4><input type="submit" value="保存修改" ></h4></td>
							
					</tr>
				</tbody>
			</table>
		</form>
	</div>
					
					</div>
				
				<div class="clearfix"> </div>
		

</body>
</jsp>