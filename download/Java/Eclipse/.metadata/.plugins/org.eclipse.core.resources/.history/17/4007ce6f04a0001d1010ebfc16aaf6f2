package Model;

import java.util.ArrayList;
public class Usuario {
    private String nome;
    private String cpf;
    private float salario;
    private ArrayList<Contas> contas;
    
	public Usuario(String nomeU) {
		this.nome = nomeU;
		this.contas = new ArrayList<Contas>();
	}

	public String getNome() {
        return nome;
    }
	
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public String getCpf() {
        return cpf;
    }
    
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    
    public float getSalario() {
        return salario;
    }
    
    public void setSalario(float salario) {
        this.salario = salario;
    }
    
    public void adicionarConta(Contas conta) {
    	this.contas.add(conta);
    }
    
    public float somarContas(){
        float a=0;
        for(int i=0; i < this.contas.size(); i++){
            a += this.contas.get(i).getValor();
        }
        return a;
    }
    
    public String mostrarContas(){
        String cabecalho = "<<<<Contas de "+this.getNome()+">>>>\n"+this.situação()+"\n";
        String relatorio = "";
        if (this.contas.size() != 0){
        	
        	for(int a=0; a < this.contas.size(); a++){
        		relatorio += (""+this.contas.get(a).getDescricao()+"-"+this.contas.get(a).getCodigo()+"\n"+
                               		"Vencimento: "+this.contas.get(a).getMes()+"/"+this.contas.get(a).getAno()+"\n"
                               		+"Valor: R$"+(this.contas.get(a).getValor()+"\n"));
            }
        }
        return cabecalho+relatorio;
        }

    protected String situação() {
    	String s = "";
    	if (this.salario < this.somarContas()) {
    		s =  "USUARIO ENDIVIDADO!!!";
    	}else {s = "Tudo certo :)";};
    	return s;
    }
    
    public void pagarConta(String codigo) {
    	int x = -1;
    	do {
    		x++;
    	}while(!this.contas.get(x).getCodigo().equals(codigo));
    	
    	float novoSalario = this.getSalario() - this.contas.get(x).getValor();
    	this.salario = novoSalario;
    	this.contas.remove(x);
    	
    }
}
