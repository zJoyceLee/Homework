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
					<td><h4>订单号</h4></td>	
					<td><h4>订单日期</h4></td>		
					<td><h4>商品名</h4></td>
					<td><h4>商品数量</h4></td>
					<td><h4>订单总价</h4></td>	
					<td><h4>订单状态</h4></td>							
				
		<%
			Class.forName("com.mysql.jdbc.Driver");
			Connection ct = DriverManager.getConnection("jdbc:mysql://localhost:3306/shoppingSystem","root","1");	
			PreparedStatement pstmt=ct.prepareStatement("select * from Orders where username=? and status=?");
			PreparedStatement pstmt1;
			pstmt.setString(1, user.getUsername());
			pstmt.setInt(2,0);
			ResultSet rs=pstmt.executeQuery();
            ResultSet rs1;
			while (rs.next()) {
		%>
			<tr>
				<td>&nbsp;</td>
				<td><h4><%=rs.getString("order_id")%></h4></td>
				<td><h4><%=rs.getString("order_date")%></h4></td>
				<td>
				<%
					pstmt1=ct.prepareStatement("select * from OrdersInfo where order_id=?");
					pstmt1.setString(1,rs.getString("order_id"));
					rs1=pstmt1.executeQuery();
				    while (rs1.next()) {
				    %>
				<h4><%=rs1.getString("commodity_id")%><br></h4>
				<%} %>
				</td>
				<td>
				<%
					pstmt1=ct.prepareStatement("select * from OrdersInfo where order_id=?");
					pstmt1.setString(1,rs.getString("order_id"));
					rs1=pstmt1.executeQuery();
				    while (rs1.next()) {
				    %>
				<h4><%=rs1.getInt("counter")%><br></h4>
				<%} %>
				</td>
	
				<td><h4><%=rs.getString("total")%></h4></td>
				<td><h4>未发货</h4></td>
			</tr>
		<%
			}
			ct.close();
		%>
				</tbody>
			</table>
		</form>
					
				
				<div class="clearfix"> </div>
		

</body>
</jsp>