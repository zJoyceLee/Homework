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
			int num=0;

%>
	<!-- main content start-->
	<div id="page-wrapper">
		<!--banner-->
		<div class="banner about-banner">
			<div class="banner-right">
				<h1 class="wow zoomIn animated" data-wow-delay=".5s"><a href="index.html">SONY</a></h1>
			</div>
			<div class="banner-left">
				<!--navigation-->
				<nav> 
					<a href="" id="menuToggle"> <span class="navClosed"></span> </a>
					<a href="index.jsp">首页</a> 
					<a href="products.jsp">全部商品</a> 
					<a href="contact.jsp" class="active">关于我们</a> 
				</nav>
				<script>
					(function($){
						// Menu Functions
						$(document).ready(function(){
						$('#menuToggle').click(function(e){
							var $parent = $(this).parent('nav');
						  $parent.toggleClass("open");
						  var navState = $parent.hasClass('open') ? "hide" : "show";
						  $(this).attr("title", navState + " navigation");
								// Set the timeout to the animation length in the CSS.
								setTimeout(function(){
									console.log("timeout set");
									$('#menuToggle > span').toggleClass("navClosed").toggleClass("navOpen");
								}, 200);
							e.preventDefault();
						});
					  });
					})(jQuery);
				</script>
				<!--//navigation-->
				<div class="banner-text">
					<h2 class="wow fadeInDownBig animated" data-wow-delay=".5s">索尼相机 <br>专营网站 </h2>
					<p class="wow fadeInUpBig animated" data-wow-delay=".5s">这里有最新最全的索尼相机，欢迎您的选购。</p>
					  
					  <ol class="breadcrumb wow fadeInUpBig animated" data-wow-delay=".5s">
					  <li><a href="index.jsp">首页</a></li>
					  <li>商品详情</li>
					</ol>
				</div>
			</div>
			<div class="clearfix"> </div>
		</div>
		<!--//banner-->
		<!-- single -->
		<div class="single">
			<div class="container">
				<%
					Class.forName("com.mysql.jdbc.Driver");
					Connection ct = DriverManager.getConnection("jdbc:mysql://localhost:3306/shoppingSystem","root","1");	
					PreparedStatement pstmt=ct.prepareStatement("select * from Commodity where id=?"); 
					pstmt.setString(1,id);
					ResultSet rs=pstmt.executeQuery();
					while (rs.next()) {
				%>
				<h3 class="title wow fadeInDown animated" data-wow-delay=".5s">Goods Details</h3>
				<div class="single-page-artical">
					<div class="artical-content">
					
						<h2 class="wow fadeInDown animated" data-wow-delay=".5s"><%=rs.getString("name")%></h2>
						<br>
						<br>
						<% 
					    	PreparedStatement pstmt1=ct.prepareStatement("select img_path from Image where commodity_id=? and img_path like?"); 
							pstmt1.setString(1,rs.getString("id"));
							pstmt1.setString(2,"%"+"_1"+"%");
							ResultSet rs1=pstmt1.executeQuery();
							while (rs1.next()) {
						%>
    				  	<img src="images/<%=rs1.getString("img_path")%>"></img>
						<%
							}
						%>
					</div>
		<div class="contact-form">
			
		<table class="table table-striped" width="100">
			<tr>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td>&nbsp;&nbsp;&nbsp;</td>
			<td><h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;¥<%=rs.getInt("price")%>.00</h1></td>
			
			</tr>
			<tr>
				<td>&nbsp;&nbsp;&nbsp;</td>		
				<td>&nbsp;&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;&nbsp;</td>
				<td>
				<br>
				<br>
				
					<form action ="http://localhost:8080/shopping/html/add.jsp" >
					<h3>
					<select name="num" id="num">
  						<option value="1">&nbsp; 1 &nbsp;</option>
  						<option value="2">&nbsp; 2 &nbsp;</option>
  						<option value="3">&nbsp; 3 &nbsp;</option>
  						<option value="4">&nbsp; 4 &nbsp;</option>
  						<option value="5">&nbsp; 5 &nbsp;</option>
  						<option value="6">&nbsp; 6 &nbsp;</option>
  						<option value="7">&nbsp; 7 &nbsp;</option>
  						<option value="8">&nbsp; 8 &nbsp;</option>
  						<option value="9">&nbsp; 9 &nbsp;</option>
					</select>
					&nbsp;
					库存：<%=rs.getInt("store")%>
					</h3>
					
				</td>
			
				</td>	
			
				
				<td>
				
					
					 <input type="hidden" name="id" value="<%=request.getParameter("id")%>"/>
					<h3><input type="submit" value="加入购物车" ></h3>
					</form>
				</td>
													
			</tr>	
		</table>
	</div>
	
		<div class="information" id="information">
			<br>
			<br>
					
					<div class="artical-links fadeInDown animated" data-wow-delay=".5s">
						<ul>
						<div class="bs-docs-example wow fadeInDown animated" data-wow-delay=".5s">
					
						<h3><%=rs.getString("info")%></h3>
	
						</div>
						<% 
					    	PreparedStatement pstmt2=ct.prepareStatement("select img_path from Image where commodity_id=? and img_path like?"); 
							pstmt2.setString(1,rs.getString("id"));
							pstmt2.setString(2,"%"+"_2"+"%");
							ResultSet rs2=pstmt2.executeQuery();
							while (rs2.next()) {
						%>
    				  	<img src="images/<%=rs2.getString("img_path")%>"></img>

						<%
							}
						%>	
						<% 
					    	pstmt2=ct.prepareStatement("select img_path from Image where commodity_id=? and img_path like?"); 
							pstmt2.setString(1,rs.getString("id"));
							pstmt2.setString(2,"%"+"_3"+"%");
							rs2=pstmt2.executeQuery();
							while (rs2.next()) {
						%>
    				  	<img src="images/<%=rs2.getString("img_path")%>"></img>

						<%
							}
						%>			
					</ul>
				</div>
			</div>
		 <%
			}
		 %>
	
				
		
	
				</div>
			</div>
		</div>
		<!-- //single -->
		<!--footer-->
		<div class="footer">
			<div class="container">
				<div class="col-md-4 footer-grids wow fadeInDown animated" data-wow-delay=".5s">
					<h3>Review :</h3>
					<p>Sed ut turpis elit ullamcorper in auctor non, accumsan vel lacus nulla auctor cursus nunc. Maecenas ultricies dolor in urna tempus, id egestas erat finibus  interdum lectus eget scelerisque.</p>
				</div>
				<div class="col-md-4 footer-grids footer-address wow fadeInDown animated" data-wow-delay=".5s">
					<h3>Contact Us:</h3>
					<ul>
						<li><i class="glyphicon glyphicon-send"></i> 中国上海市鲁班路288号  <span> 星光摄影器材城c区一楼173号 </span></li>
						<li><i class="glyphicon glyphicon-phone"></i> 021-53862718 </li>
						<li><i class="glyphicon glyphicon-envelope"></i><a href="mailto:example@mail.com">mail@example.com</a></li>
					</ul>
				</div>
				<div class="col-md-4 footer-grids wow fadeInDown animated" data-wow-delay=".5s">
					<h3>Follow us:</h3>
					<ul>
						<li><a href="#"><img src="images/f1.png" alt=""> FACEBOOK</a></li>
						<li><a href="#"><img src="images/f2.png" alt=""> GOOGLE+</a></li>
						<li><a href="#"><img src="images/f3.png" alt=""> LINKEDIN</a></li>
						<li><a href="#"><img src="images/f4.png" alt=""> TWITTER</a></li>
					</ul>
				</div>
				<div class="clearfix"> </div>
			</div>
		</div>
		<!--//footer-->

	</div>
	<!--//main content start-->
	<!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/bootstrap.js"></script>
</body>
</jsp>