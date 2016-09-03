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
			// �����������
			request.setCharacterEncoding("utf-8");
			// ������Ӧ����
			response.setContentType("utf-8");
			
			String phone=request.getParameter("phone");
			String addr=request.getParameter("addr");
			String email=request.getParameter("email");
			// ����DB�����ʹ�����еķ���������ж�
			Mysql sql=new Mysql();
			// ���session��������������Ϣ
			HttpSession session=request.getSession();
			// �Ȼ��user��������ǵ�һ�η��ʸ�Servlet���û�����϶�Ϊ�գ�������ǵ�
			// ���������ǵ����Σ��Ͳ�Ӧ�����жϸ��û�����Ϣ
			User user=(User) session.getAttribute("user");
			// ��������жϣ�����û��ǵ�һ�ν��룬����DataBase���еķ����ж�
			if(user==null){
				// ������ݲ�ѯ���û�Ϊ�գ���ʾ�û�����������ȷ��Ӧ��ȥ����ҳ
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

