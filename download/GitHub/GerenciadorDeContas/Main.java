//Feito por: David Augusto de Oliveira e Silva
//Gerenciador de Contas v1.0

import javax.swing.JOptionPane;import java.util.ArrayList;
public class Main{
    public static void main(String args[]){
      String op="";//OPÇÃO DO MENU PRINCIPAL
      ArrayList<Usuario> usuarios = new ArrayList<Usuario>();
      
      
      do{//MENU PRINCIPAL
    	 String listaUsuarios = "";
	     if (usuarios.size() != 0) {
           for(int x=0; x < usuarios.size(); x++ ) {
         	  
         	  listaUsuarios += usuarios.get(x).getNome()+" - "+
         			  		   usuarios.get(x).getCpf()+"\n"+
         			  		   "Salario Líquido: R$"+usuarios.get(x).getSalario()+"\n\n";}}
	     
    	  op = JOptionPane.showInputDialog(null, listaUsuarios+
    		  									"Escolha uma opcão:\n"+
    				  							"[1]\t Cadastrar usuário  "+
    				  							"[2]\t Mostrar contas de um usuário  "+
    		  									"[0]\t Encerrar Programa");
      		
         if(Integer.parseInt(op) == 1){// CADASTRAR NOVO USUARIO
           String nomeUsuario = JOptionPane.showInputDialog("Nome do Usuário");
           Usuario u = new Usuario(nomeUsuario);
           u.setCpf(JOptionPane.showInputDialog("CPF"));
           u.setSalario(Float.parseFloat(JOptionPane.showInputDialog("Salario Líquido")));
           usuarios.add(u);}//Fim do bloco cADASTRAR NOVO USUARIO
         
         if(Integer.parseInt(op) == 2){//CONTAS DO USUARIO
        	 
           // Pesquisa do usuário através do CPF
           String cpfUsuario = JOptionPane.showInputDialog("Insira o CPF do Usuario");int i = -1;
           do {
        	   i++;
           }while (!usuarios.get(i).getCpf().equals(cpfUsuario));
           ;
           
         // MENU DE CONTAS DO USUARIO  
         int opcao;
		 do {opcao = -1;
        	   opcao = Integer.parseInt(JOptionPane.showInputDialog(null, usuarios.get(i).mostrarContas()+"\n\n"+
        			   					"[0] Voltar ao menu inicial "+
        			   					"[1] Adicionar conta "+
        			   					"[2] Pagar conta"));
        	   
        	   if (opcao == 1) {// Adicionar Conta a pagar
        		   Contas c = new Contas();
        		   c.setDescricao(JOptionPane.showInputDialog(null, "Insira a descrição da conta"));
        		   c.setCodigo(JOptionPane.showInputDialog(null, "Insira o código da conta (13 dígitos)"));
        		   c.setValor(Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o valor da conta")));
        		   c.setMes(Integer.parseInt(JOptionPane.showInputDialog(null, "Mês de vencimento")));
        		   c.setAno(Integer.parseInt(JOptionPane.showInputDialog(null, "Ano de vencimento")));
        		   usuarios.get(i).adicionarConta(c);}
        	   
        	   if (opcao == 2) {// Pagar conta
        		  String codigo = JOptionPane.showInputDialog(null, "Insira o código da conta a pagar");
        		  usuarios.get(i).pagarConta(codigo);}
        	   
           }while(opcao != 0); // 
           }//Fim do bloco CONTAS DO USUARIO
         
        if(op.equals("")||Integer.parseInt(op)>2) {continue;}
         
      }while(Integer.parseInt(op) != 0);
      
      System.exit(0);}
      // Fim do programa
}