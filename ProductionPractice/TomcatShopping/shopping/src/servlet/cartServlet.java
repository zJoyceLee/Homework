	package servlet;

	import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;

	import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

	import javaBean.User;
import dataBase.Mysql;
	
public class cartServlet extends HttpServlet {
	
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// �����������
		request.setCharacterEncoding("utf-8");
		// ������Ӧ����
		response.setContentType("utf-8");
		String id[]=request.getParameterValues("commodity_id");
		int i=0;
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
			sql.upOrder(user.getUsername());
			
			for(i=0;i<id.length;i++){
				System.out.println("!!!!"+id[i]+"!!!!!");
			    sql.upOrderinfo(user.getUsername(),id[i],sql.getOrder_id(user.getUsername()));
			    //sql.upCounter(user.getUsername(), id[i], sql.getOrder_id(user.getUsername()));
			}
			
	
				try {
					sql.delCart(user.getUsername());
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			
			
			response.sendRedirect("http://localhost:8080/shopping/html/user.jsp#orders");
		}
		
		
		
	}
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request,response);
		}
	}

