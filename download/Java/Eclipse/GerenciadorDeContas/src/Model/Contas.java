package Model;
public class Contas {

    private String codigo;
    private float valor;
    private String descricao;
    private int mes; private int ano;
    

    public Contas() {
    }
    
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public float getValor() {
        return valor;
    }

    public void setValor(float valor) {
        this.valor = valor;
    }

    public String getDescricao() {
        return descricao;
    }
   
    public int getMes() {
		return mes;
	}

	public int getAno() {
		return ano;
	}

	public void setMes(int mes) {
		this.mes = mes;
	}

	public void setAno(int ano) {
		this.ano = ano;
	}

	public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
}