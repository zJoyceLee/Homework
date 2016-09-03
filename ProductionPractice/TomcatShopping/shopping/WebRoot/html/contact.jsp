<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<jsp>
<head>
<title>关于我们</title>
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
</head>
<body>
<%
			request.setCharacterEncoding("utf-8");
			response.setCharacterEncoding("utf-8");
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
					  <li>关于我们</li>
					</ol>
				</div>
			</div>
			<div class="clearfix"> </div>
		</div>
		<!--//banner-->
		<!--contact-->
		<div class="map">
			<iframe class="wow fadeInUp animated" data-wow-delay=".5s" src="http://www.google.cn/maps/embed?pb=!1m18!1m12!1m3!1d853.1587727936809!2d121.4739687291964!3d31.20312974593747!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xe673b5cef8a5d792!2z5pif5YWJ5pGE5b2x5Zmo5p2Q5Z-O!5e0!3m2!1szh-CN!2scn!4v1467334761722" allowfullscreen></iframe>
		</div>
		<div class="contact">
			<div class="container">
				<div class="contact-info">
					<div class="col-md-4 contact-grids">
						<div class="cnt-address wow slideInLeft animated" data-wow-delay=".5s">
							<br>
							<br>
							<h3 class="title">联系我们：</h3>
							<p>联系地址：中国上海市鲁班路288号 
							   <span>&nbsp;&nbsp;星光摄影器材城c区一楼173号</span>
								<span>联系电话：021-53862718</span>
								电子邮箱： <a href="mailto:info@example.com">mail@example.com</a>
							</p>
						</div>
					</div>
					<div class="col-md-8 contact-grids wow slideInRight animated" data-wow-delay=".5s">
						<div class="contact-form">
							<h3 class="title">投诉与建议：</h3>
							<form>
								<textarea placeholder="输入您想说的话..." required=""></textarea>
								<input type="text" placeholder="姓名" required="">
								<input type="text" placeholder="电子邮件" required="">
								<input type="submit" value="发送">
							</form>
						</div>
					</div>
					<div class="clearfix"> </div>
				</div>
			</div>
		</div>
		<!--//contact-->
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
</html>