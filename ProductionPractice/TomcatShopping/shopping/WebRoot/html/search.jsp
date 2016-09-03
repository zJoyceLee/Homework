<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<jsp>
<title>搜索商品</title>

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
<!--picture-->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="css/lanrenzhijia.css"></link>
<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="js/lanrenzhijia.js"></script>
<!--//picture-->
<%@page import='java.sql.*' %>
</head>
<body>
<%
			request.setCharacterEncoding("utf-8");
			response.setCharacterEncoding("utf-8");
			String search=request.getParameter("search");
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
					<a href="#home" class="active">搜索</a> 
					<a href="products.jsp">全部商品</a> 
					<a href="contact.jsp">关于我们</a> 
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
					  <li><a href="http://localhost:8080/shopping/servlet/loginServlet">首页</a></li>
					  <li>为您找到以下商品</li>
					</ol>
				</div>
			</div>
			<div class="clearfix"> </div>
		</div>
		<!--//banner-->
		<!-- products -->
		<div class="single">
			<div class="container">
				<h3 class="title wow fadeInDown animated" data-wow-delay=".5s">Something You Many Want</h3>
				<div class="galleryContainer">
					<%
						Class.forName("com.mysql.jdbc.Driver");
						Connection ct = DriverManager.getConnection("jdbc:mysql://localhost:3306/shoppingSystem","root","1");	
						PreparedStatement pstmt=ct.prepareStatement("select * from Commodity where name like ?"); 
						pstmt.setString(1,"%"+search+"%");
						ResultSet rs=pstmt.executeQuery();
						while (rs.next()) {
					%>
					<!--galleryEntry-->    
					<a href="http://localhost:8080/shopping/html/details.jsp?id=<%= rs.getString("id") %>">
					<div class="galleryImage">
					<% 
					PreparedStatement pstmt1=ct.prepareStatement("select img_path from Image where commodity_id=?"); 
						pstmt1.setString(1,rs.getString("id"));
						ResultSet rs1=pstmt1.executeQuery();
						while (rs1.next()) {
						
						%>
    				  	<img src="images/<%=rs1.getString("img_path")%>"></img>
    				  	<%
						}
    				  	%>
     					<div class="info">  
         					<h2>¥<%=rs.getInt("price")%>.00</h2>
         					<p>
              				<%=rs.getString("name")%>
          					</p>
      					</div>
    				</div>
    				</a>>
					<!--end galleryEntry--> 
				 <%
				 } 
				 %>
  				</div>
 			</div>
		</div>
	</div>
	<!-- //products -->
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