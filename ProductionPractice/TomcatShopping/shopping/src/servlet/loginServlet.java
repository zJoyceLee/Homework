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

import java.security.*;


public class loginServlet extends HttpServlet {
public void doGet(HttpServletRequest request, HttpServletResponse response)
		throws ServletException, IOException {
	// 设置请求编码
	request.setCharacterEncoding("utf-8");
	// 设置响应编码
	response.setContentType("utf-8");
	// 获得JSP页面输入的用户名的值
	String username=request.getParameter("username");
	// 获得JSP页面输入的密码的值
	String password=request.getParameter("password");
	
      
// 建立DB类对象，使用其中的方法来完成判断
	Mysql sql=new Mysql();
	// 获得session对象，用来保存信息
	HttpSession session=request.getSession();
	// 先获得user对象，如果是第一次访问该Servlet，用户对象肯定为空，但如果是第
	// 二次甚至是第三次，就不应该再判断该用户的信息
	User user=(User) session.getAttribute("user");
	// 这里就是判断，如果用户是第一次进入，调用DataBase类中的方法判断
	if(user==null){
		
		  String result = "";
	        try {
	            MessageDigest md = MessageDigest.getInstance("MD5");
	            md.update(password.getBytes());
	            byte b[] = md.digest();
	            int i;
	            StringBuffer buf = new StringBuffer("");
	            for (int offset = 0; offset < b.length; offset++) {
	                i = b[offset];
	                if (i < 0)
	                    i += 256;
	                if (i < 16)
	                    buf.append("0");
	                buf.append(Integer.toHexString(i));
	            }
	            result = buf.toString();
	            
	        } catch (NoSuchAlgorithmException e) {
	            System.out.println(e);
	        }
	    
		 user=sql.checkUser(username, result);
	}
	// 把user对象存在session中
	session.setAttribute("user", user);

	if(user!=null){
		// 如果根据查询，用户不为空，表示用户名和密码正确，应该去下一界面
		user.setPhone(sql.getPhone(username));
		user.setAddr(sql.getAddr(username));
		user.setEmail(sql.getEmail(username));
		
		response.sendRedirect("http://localhost:8080/shopping/html/login.jsp");
	}else{
		// 如果用户名和密码错误，回到登录界面
		response.sendRedirect("http://localhost:8080/shopping/html/index.jsp?error=yes");
	}
}
public void doPost(HttpServletRequest request, HttpServletResponse response)
		throws ServletException, IOException {
	doGet(request,response);
	}
}
