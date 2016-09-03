package dataBase;

import java.sql.*;

import javaBean.User;

import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class Mysql {
	Connection ct;
	PreparedStatement pstmt;
	// �ڹ��캯���н�������ݿ�����ӣ������ڽ���DB����ʱ����������ݿ�
	
	public Mysql(){
		try {
			
			Class.forName("com.mysql.jdbc.Driver");
				ct=DriverManager.getConnection
				("jdbc:mysql://localhost:3306/shoppingSystem?useUnicode=true&characterEncoding=UTF-8","root","1");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// ���userName��password��ѯ�û����鵽�ͷ��ظö���û�оͷ���null
	public User checkUser(String username,String result){
		try{
		pstmt=ct.prepareStatement("select * from User where username=? and password=?");
			pstmt.setString(1, username);
			pstmt.setString(2, result);
			ResultSet rs=pstmt.executeQuery();
			
			User user=new User();
			while(rs.next()){
				user.setUsername(rs.getString(1));
				user.setPassword(rs.getString(2));
				return user;
			}
			return null;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}
	}
		
		public String getPhone(String username){
			String phone=null;
			try{
				pstmt=ct.prepareStatement("select phone from User where username=?");
				pstmt.setString(1, username);
				ResultSet rs=pstmt.executeQuery();
				while(rs.next()){
					 phone=rs.getString(1);
				}
				return phone;
			}catch(Exception e){
				e.printStackTrace();
				return null;
			}
		}
		public String getAddr(String username){
			String addr=null;
			try{
				pstmt=ct.prepareStatement("select addr from User where username=?");
				pstmt.setString(1, username);
				ResultSet rs=pstmt.executeQuery();
				while(rs.next()){
					 addr=rs.getString(1);
				}
				return addr;
			}catch(Exception e){
				e.printStackTrace();
				return null;
			}
		}
		public String getEmail(String username){
			String email=null;
			try{
				pstmt=ct.prepareStatement("select email from User where username=?");
				pstmt.setString(1, username);
				ResultSet rs=pstmt.executeQuery();
				while(rs.next()){
					 email=rs.getString(1);
				}
				return email;
			}catch(Exception e){
				e.printStackTrace();
				return null;
			}
		}
	
		public void setPhone(String phone,String username){
			try{
				pstmt=ct.prepareStatement("update User set phone =? where username=?");
				pstmt.setString(1, phone);
				pstmt.setString(2, username);
				pstmt.executeUpdate();
				
			}catch(Exception e){
				e.printStackTrace();	
			}
		}
		
		public void setAddr(String addr,String username){
			try{
				pstmt=ct.prepareStatement("update User set addr =? where username=?");
				pstmt.setString(1, addr);
				pstmt.setString(2, username);
				pstmt.executeUpdate();
				
			}catch(Exception e){
				e.printStackTrace();	
			}
		}
		public void setEmail(String email,String username){
			try{
				pstmt=ct.prepareStatement("update User set email =? where username=?");
				pstmt.setString(1, email);
				pstmt.setString(2, username);
				pstmt.executeUpdate();
				
			}catch(Exception e){
				e.printStackTrace();	
			}
		}


public void upOrderinfo(String username,String id,int order_id){
	try{
		int counter;
		pstmt=ct.prepareStatement("select counter from ShoppingCart where username=? and commodity_id=?");
		pstmt.setString(1, username);
		pstmt.setString(2, id);
		ResultSet rs=pstmt.executeQuery();
		while(rs.next()){
			counter = rs.getInt("counter");
			PreparedStatement pstmt1=ct.prepareStatement("insert into OrdersInfo values(?,?,?)");
			pstmt1.setInt(1, order_id);
			pstmt1.setString(2, id);
			pstmt1.setInt(3, counter);
			pstmt1.executeUpdate();
		}
		
	}catch(Exception e){
		e.printStackTrace();
	
	}
}
public String upOrder(String username){
	try{
		DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
	       //get current date time with Date()
	       Date date = new Date();
	       pstmt=ct.prepareStatement("insert into Orders(order_date,status,username) values(?,?,?) ");
	       pstmt.setString(1, dateFormat.format(date));
	       pstmt.setInt(2, -1);
	       pstmt.setString(3, username);
	       pstmt.executeUpdate();
		return dateFormat.format(date);
	}catch(Exception e){
		e.printStackTrace();
		return null;
	}
}
public int getOrder_id(String username){
	int id=0;
	try{
		pstmt=ct.prepareStatement("select MAX(order_id) from Orders where username=?");
		pstmt.setString(1, username);
		ResultSet rs=pstmt.executeQuery();
		while(rs.next()){
			 id=rs.getInt(1);
		}
		return id;
	}catch(Exception e){
		e.printStackTrace();
		return 0;
	}
}
public void delCart(String username) throws SQLException {
	
		 PreparedStatement stmt = ct.prepareStatement("delete from ShoppingCart where username = ?");
		 stmt.setString(1, username);
		 stmt.addBatch();
		 stmt.executeBatch();
	
}
public void upCounter(String username,String id,int order_id){
	try{
		int num=0;
		int counter=0;
		pstmt=ct.prepareStatement("select counter from Commodity where id=?");
		pstmt.setString(1, id);
		ResultSet rs=pstmt.executeQuery();
		counter = rs.getInt("counter");
		while(rs.next()){
			PreparedStatement pstmt1=ct.prepareStatement("select counter from ShoppingCart where username=? and commodity_id=?");
			pstmt1.setString(1, username);
			pstmt1.setString(2, id);
			ResultSet rs1=pstmt1.executeQuery();
			num = rs.getInt("counter");
			if(counter>=num){
			PreparedStatement pstmt2=ct.prepareStatement("update Commodity set counter=? where id=?");
			pstmt2.setInt(1,counter-num);
			pstmt2.setString(2, id);
			pstmt2.executeUpdate();
			}	
		}
	}catch(Exception e){
		e.printStackTrace();	
		}
	}
	
}

//	public void dealShopping(User user, String productIds[]) throws SQLException {
//		pstmt = ct.prepareStatement("insert into shopRecords(userId, productId, number, shopDate) values(?, ?, ?, ?)");
//		pstmt.setInt(1, user.getId());
//		for(String str : productIds) {
//	        pstmt.setInt(2, Integer.parseInt(str));
//	        pstmt.setInt(3, 1);
//	        pstmt.setDate(4, new Date(System.currentTimeMillis()));
//	        pstmt.addBatch();
//		}
//		pstmt.executeBatch();
//	}
//	

//	
//	
//	public void operateUser(User user, String str) throws SQLException {
//      if(str.equals("add")) {
//          PreparedStatement stmt = ct.prepareStatement("insert into usertTable(userName, password) values(?, ?)");
//          stmt.setString(1, user.getUserName());
//          stmt.setString(2, user.getPassword());
//          stmt.executeUpdate();
//        }
//        else if(str.equals("del")) {
//          PreparedStatement stmt = ct.prepareStatement("delete from userTable where id = ?");
//          stmt.setInt(1, user.getId());
//          stmt.addBatch();
//          stmt.executeBatch();
//        }
//	}
//}
//
//

	
	
//	
//	//����û���

//	
//		//����û�����
//		public String getPassword(int id){
//			String password=null;
//			try{
//				pstmt=ct.prepareStatement("select password from [user] where id=?");
//				pstmt.setInt(1, id);
//				ResultSet rs=pstmt.executeQuery();
//				while(rs.next()){
//					 password=rs.getString(1);
//				}
//				return password;
//			}catch(Exception e){
//				e.printStackTrace();
//				return null;
//			}
//	}
//
//		
//		//�����Ʒ����
//		public String getProductCode(int id){
//			String productCode=null;
//			try{
//				pstmt=ct.prepareStatement("select productCode from [productTable] where id=?");
//				pstmt.setInt(1, id);
//				ResultSet rs=pstmt.executeQuery();
//				while(rs.next()){
//					 productCode=rs.getString(1);
//				}
//				return productCode;
//			}catch(Exception e){
//				e.printStackTrace();
//				return null;
//			}
//		}
//		
//		//�����Ʒ��
//		public String getProductName(int id){
//			String productName=null;
//			try{
//				pstmt=ct.prepareStatement("select productName from [productTable] where id=?");
//				pstmt.setInt(1, id);
//				ResultSet rs=pstmt.executeQuery();
//				while(rs.next()){
//					 productName=rs.getString(1);
//				}
//				return productName;
//			}catch(Exception e){
//				e.printStackTrace();
//				return null;
//			}
//		}
//		
//		//�����Ʒ��
//		public String getProductSource(int id){
//			String productSource=null;
//			try{
//				pstmt=ct.prepareStatement("select productSource from [productTable] where id=?");
//				pstmt.setInt(1, id);
//				ResultSet rs=pstmt.executeQuery();
//				while(rs.next()){
//					 productSource=rs.getString(1);
//				}
//				return productSource;
//			}catch(Exception e){
//				e.printStackTrace();
//				return null;
//			}
//		}
//		
//		
//		//���û����������
//		public boolean addUser(User u){
//			try{
//				pstmt=ct.prepareStatement("insert into [user] values(?,?,?)");
//				pstmt.setInt(1, u.getId());
//				pstmt.setString(2, u.getUserName());
//				pstmt.setString(3, u.getPassword());
//				pstmt.executeUpdate();
//				return true;
//			}catch(Exception e){
//				e.printStackTrace();
//				return false;
//			}
//		}
//		
//		//����Ʒ���������
//				public boolean addProduct(Product p){
//					try{
//						pstmt=ct.prepareStatement("insert into [productTable] values(?,?,?,?)");
//						pstmt.setInt(1, p.getId());
//						pstmt.setString(2, p.getProductCode());
//						pstmt.setString(3, p.getProductName());
//						pstmt.setString(4, p.getProductSource());
//						pstmt.executeUpdate();
//						return true;
//					}catch(Exception e){
//						e.printStackTrace();
//						return false;
//					}
//				}
//
//		
//}
