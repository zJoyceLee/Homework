<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<jsp>
<head>
<title>商品详情</title>
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
<!--web-fonts-->
<link href='//fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>
<link href='//fonts.googleapis.com/css?family=Slabo+27px' rel='stylesheet' type='text/css'>
<link href='//fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>
<!--//web-fonts-->
<!--animate-->
<link href="css/animate.css" rel="stylesheet" type="text/css" media="all">
<script src="js/wow.min.js"></script>
	<script>
		 new WOW().init();
	</script>
<!--//end-animate-->
<!-- start-smoth-scrolling-->
<script type="text/javascript">
		jQuery(document).ready(function($) {
			$(".scroll").click(function(event){		
				event.preventDefault();
				$('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
			});
		});
</script>
<!--//end-smoth-scrolling-->
<%@ page language="java" import="javaBean.User"%>
<%@page import='java.sql.*' %>
</head>
<body>
<%
			request.setCharacterEncoding("utf-8");
			response.setCharacterEncoding("utf-8");
%>
<%		
			User user = (User) session.getAttribute("user");
			
			String id=(String)request.getParameter("id");
			String num =(String)request.getParameter("num");
			System.out.println(num+"!!!!!!!!!!!!");
			int counter=Integer.valueOf(num);	
				boolean flag= false;
				int counter1=0;
				Class.forName("com.mysql.jdbc.Driver");
				Connection ct=DriverManager.getConnection("jdbc:mysql://localhost:3306/shoppingSystem","root","1");
				PreparedStatement pstmt1=ct.prepareStatement("select counter from ShoppingCart where username=? and commodity_id=?");
				pstmt1.setString(1, user.getUsername());
				pstmt1.setString(2, id);
				ResultSet rs1=pstmt1.executeQuery();
				while(rs1.next()){
					flag = true;
					counter1=rs1.getInt(1);
		 			PreparedStatement pstmt2=ct.prepareStatement("update ShoppingCart set counter=? where username=? and commodity_id=?"); 
					pstmt2.setString(2,user.getUsername());
					pstmt2.setString(3,id);
	       		 	pstmt2.setInt(1,counter+counter1);
	        		pstmt2.executeUpdate();

				}

					if(flag==false)	{	
					PreparedStatement pstmt3=ct.prepareStatement("insert into ShoppingCart values(?,?,?)"); 
					pstmt3.setString(1,user.getUsername());
					pstmt3.setString(2,id);
					pstmt3.setInt(3,counter);
					pstmt3.executeUpdate();
					}
	 		
	 		%>
	 		<div class="contact-form">
	
		<table class="table table-striped" width="100">
	
			<tr>
				<td>&nbsp;</td>
				<form action ="http://localhost:8080/shopping/html/details.jsp" >
				<td>
					 <input type="hidden" name="id" value="<%=request.getParameter("id")%>"/>
					<br>
					<h1>加入成功请返回</h1>
				</td>
				<td>&nbsp;</td>		
				<td>
				
					<h3><input type="submit" value="返回商品界面" ></h3>
					
				</td>
				</form>
				<td>&nbsp;</td>
				<form action="http://localhost:8080/shopping/html/cart.jsp" method="post">
				<td>
					
					<h3><input type="submit" value="查看购物车" ></h3>
					
					</td>
					</form>
				<td>&nbsp;</td>									
			</tr>	
		</table>
			 		

</body>
</jsp>