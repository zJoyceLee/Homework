<!DOCTYPE html>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<jsp>
<head>
<title>购物网站 </title>
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
<link rel="stylesheet" href="css/lightbox.css">
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
<!--display products-->
<link type="text/css" rel="stylesheet" href="css/carousel.css">
<!--//display products-->

<script> 
//取出传回来的参数error并与yes比较
  var errori ='<%=request.getAttribute("error")%>';
  if(errori=='yes'){
   alert("登录失败!");
  }
</script>

</head>
<body>
	<%
			request.setCharacterEncoding("utf-8");
			response.setCharacterEncoding("utf-8");
	%>
	<!-- main content start-->
	<div id="page-wrapper">
		<!--banner-->
		<div class="banner" id="home">
			<div class="banner-right">
			<h1 class="wow zoomIn animated" data-wow-delay=".5s"><a href="index.jsp">welcome</a></h1>
			</div>
			<div class="banner-left">
				<!--navigation-->
				<nav> 
					<a href="" id="menuToggle"> <span class="navClosed"></span> </a>
					<a href="#home" class="active scroll">首页</a>  
					<a href="#gallery" class="scroll">精选商品</a> 
					<a href="#blog" class="scroll">搜索</a>
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
					<h2 class="wow fadeInDownBig animated" data-wow-delay=".5s">索尼相机 <br>专营网站 <br> 欢迎您的点击</h2>
					<p class="wow fadeInUpBig animated" data-wow-delay=".5s">这里有最新最全的索尼相机，欢迎您的选购。</p>
					<a href="http://localhost:8000/online/regist/" class="buy btn-wayra wow zoomInRight animated" data-wow-delay=".5s">注册会员</a>
					 &nbsp; &nbsp;
					<a href="#login" class="buy btn-wayra wow zoomInRight animated" data-wow-delay=".5s">登录会员</a>
				</div>
			</div>
			<div class="clearfix"> </div>
		</div>
		<!--//banner-->
		
		<!--login-->
		<div class="login" id="login">		
			<div class="container">
			<h3 class="title">Please  Login</h3>
				<div class="blog-left1 wow fadeInDownBig animated" data-wow-delay=".5s">
					<h3 class="title wow fadeInLeftBig animated" data-wow-delay=".5s">请您登陆：</h3>
					<div class="contact-form">
						<form action="http://localhost:8080/shopping/servlet/loginServlet" method="post">
							<input name="username" type="text" placeholder="姓名" required="">
							<input name="password" type="password" placeholder="密码" required="">
							<input type="submit" value="登陆">
						</form>
					</div>	
				</div>
				<div class="clearfix"> </div>
			</div>
		</div>
		<!--//login-->
		
		<!--gallery-->
		<div class="gallery" id="gallery">		
			<h3 class="title">Something Popular</h3>
			<!-- 代码部分begin -->
			<div class="container">
				<div class="pictureSlider poster-main" data-setting='{"width":1250,"height":505,"posterWidth":500,"posterHeight":500,"scale":0.8,"autoPlay":true,"delay":2000,"speed":300}'>
					<div class="poster-btn poster-prev-btn"></div>
    					<ul class="poster-list">
    						<li class="poster-item"><a href="http://localhost:8080/shopping/html/details.jsp?id=ILCE7SM2"><img src="images/01.jpeg" width="70%" height="70%"></a></li>
      						<li class="poster-item"><a href="http://localhost:8080/shopping/html/details.jsp?id=ILCE7A72"><img src="images/02.jpeg" width="70%" height="70%"></a></li>
      						<li class="poster-item"><a href="http://localhost:8080/shopping/html/details.jsp?id=ILCE7A71"><img src="images/03.jpeg" width="70%" height="70%"></a></li>
        					<li class="poster-item"><a href="#"><img src="images/04.jpeg" width="70%" height="70%"></a></li>
        					<li class="poster-item"><a href="#"><img src="images/05.jpeg" width="70%" height="70%"></a></li>
    					</ul>
    				<div class="poster-btn poster-next-btn"></div>
				</div>
			</div>
			<script src="http://code.jquery.com/jquery-1.12.0.min.js"></script>
			<script src="js/carousel.js"></script>
			<script>
					$(function(){
						Carousel.init($(".pictureSlider"));
					});
			</script>
			<!-- 代码部分end -->
		</div>
		<!--//gallery-->
		
		<!--search-->
		<div class="blog" id="blog">		
			<div class="container">
				<h3 class="title">Search What You Want</h3>
				<div class="blog-left1 wow fadeInDownBig animated" data-wow-delay=".5s">
					<h3 class="title wow fadeInLeftBig animated" data-wow-delay=".5s">输入产品名称</h3>
					<div class="contact-form">
						<form action="http://localhost:8080/shopping/html/search.jsp" method="post">
							<input name="search" type="text" placeholder="您要查找的商品" required="">
							<input type="submit" value="查找">
						</form>
					</div>
				</div>
				<div class="clearfix"> </div>
			</div>
		</div>
		<!--//search-->
	
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
