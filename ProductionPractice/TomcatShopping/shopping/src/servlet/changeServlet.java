	package servlet;

	import java.io.IOException;
	import java.util.ArrayList;

	import javax.servlet.ServletException;
	import javax.servlet.http.HttpServlet;
	import javax.servlet.http.HttpServletRequest;
	import javax.servlet.http.HttpServletResponse;
	import javax.servlet.http.HttpSession;

	import javaBean.User;
	import dataBase.Mysql;

	public class changeServlet extends HttpServlet {
		public void doGet(HttpServletRequest request, HttpServletResponse response)
				throws ServletException, IOException {
			// 设置请求编码
			request.setCharacterEncoding("utf-8");
			// 设置响应编码
			response.setContentType("utf-8");
			
			String phone=request.getParameter("phone");
			String addr=request.getParameter("addr");
			String email=request.getParameter("email");
			// 建立DB类对象，使用其中的方法来完成判断
			Mysql sql=new Mysql();
			// 获得session对象，用来保存信息
			HttpSession session=request.getSession();
			// 先获得user对象，如果是第一次访问该Servlet，用户对象肯定为空，但如果是第
			// 二次甚至是第三次，就不应该再判断该用户的信息
			User user=(User) session.getAttribute("user");
			// 这里就是判断，如果用户是第一次进入，调用DataBase类中的方法判断
			if(user==null){
				// 如果根据查询，用户为空，表示用户名和密码正确，应该去下首页
				response.sendRedirect("http://localhost:8080/shopping/html/index.jsp?error=yes");
			}
			else{
				sql.setPhone(phone, user.getUsername());
				sql.setAddr(addr, user.getUsername());
				sql.setEmail(email, user.getUsername());
				user.setPhone(sql.getPhone(user.getUsername()));
				user.setAddr(sql.getAddr(user.getUsername()));
				user.setEmail(sql.getEmail(user.getUsername()));
				response.sendRedirect("http://localhost:8080/shopping/html/userInfo.jsp");
			}
			
			
		}
		public void doPost(HttpServletRequest request, HttpServletResponse response)
				throws ServletException, IOException {
			doGet(request,response);
			}
		}

