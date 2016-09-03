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
	// �����������
	request.setCharacterEncoding("utf-8");
	// ������Ӧ����
	response.setContentType("utf-8");
	// ���JSPҳ��������û�����ֵ
	String username=request.getParameter("username");
	// ���JSPҳ������������ֵ
	String password=request.getParameter("password");
	
      
// ����DB�����ʹ�����еķ���������ж�
	Mysql sql=new Mysql();
	// ���session��������������Ϣ
	HttpSession session=request.getSession();
	// �Ȼ��user��������ǵ�һ�η��ʸ�Servlet���û�����϶�Ϊ�գ�������ǵ�
	// ���������ǵ����Σ��Ͳ�Ӧ�����жϸ��û�����Ϣ
	User user=(User) session.getAttribute("user");
	// ��������жϣ�����û��ǵ�һ�ν��룬����DataBase���еķ����ж�
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
	// ��user�������session��
	session.setAttribute("user", user);

	if(user!=null){
		// ������ݲ�ѯ���û���Ϊ�գ���ʾ�û�����������ȷ��Ӧ��ȥ��һ����
		user.setPhone(sql.getPhone(username));
		user.setAddr(sql.getAddr(username));
		user.setEmail(sql.getEmail(username));
		
		response.sendRedirect("http://localhost:8080/shopping/html/login.jsp");
	}else{
		// ����û�����������󣬻ص���¼����
		response.sendRedirect("http://localhost:8080/shopping/html/index.jsp?error=yes");
	}
}
public void doPost(HttpServletRequest request, HttpServletResponse response)
		throws ServletException, IOException {
	doGet(request,response);
	}
}
