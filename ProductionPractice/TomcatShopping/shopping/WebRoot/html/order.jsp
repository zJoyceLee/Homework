<!DOCTYPE html >
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<jsp>
<head>
<title>订单信息</title>

<!--Custom Theme files -->
<link href="css/bootstrap.css" type="text/css" rel="stylesheet" media="all">
<link href="css/style.css" type="text/css" rel="stylesheet" media="all">
<!-- //Custom Theme files -->
<!-- js -->
<script src="js/jquery-1.11.1.min.js"></script> 
<!-- //js -->


<%@ page language="java" import="javaBean.User"%>

<style type="text/css">
body {padding: 70px;}
</style>
		<%@page import='java.sql.*' %>
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
	<div class="contact-form">
	
		<table class="table table-striped" width="100">
	
			<tr>
				<td>&nbsp;</td>
				<td>
					<form action="http://localhost:8080/shopping/html/nopay.jsp" method="post">
					<h3><input type="submit" value="未付款订单" ></h3>
					</form>
				</td>	
				<td>&nbsp;</td>		
				<td>
					<form action="http://localhost:8080/shopping/html/nosend.jsp" method="post">
					<h3><input type="submit" value="未发货订单" ></h3>
					</form>
				</td>
				<td>&nbsp;</td>
				<td>
					<form action="http://localhost:8080/shopping/html/send.jsp" method="post">
					<h3><input type="submit" value="已发货订单" ></h3>
					</form>
					</td>
				<td>&nbsp;</td>									
			</tr>	
		</table>
	</div>
			
	<div class="contact-form">
		<table class="table table-striped" width="100">
			
			<tbody>
				<tr>
								
					<td>&nbsp;</td>
					<td><h4>&nbsp;</h4></td>	
					<td><h4>&nbsp;</h4></td>		
					
					<td><h4>&nbsp;</h4></td>
					<td><h1>感谢您的付款，我们会尽快安排发货</h1></td>
					<td><h4>&nbsp;</h4></td>	
					<td><h4>&nbsp;</h4></td>							
				
		<%
			Class.forName("com.mysql.jdbc.Driver");
			Connection ct = DriverManager.getConnection("jdbc:mysql://localhost:3306/shoppingSystem","root","1");	
			PreparedStatement pstmt=ct.prepareStatement("update Orders set status=? where order_id=?");
			pstmt.setInt(1,0);
			pstmt.setString(2, request.getParameter("id"));
			pstmt.executeUpdate();
          
		%>
			
		
				</tbody>
			</table>
		</form>
					
				
				<div class="clearfix"> </div>
		

</body>
</jsp>