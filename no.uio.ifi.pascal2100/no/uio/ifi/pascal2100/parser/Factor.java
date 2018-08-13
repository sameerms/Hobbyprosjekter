package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.Main;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.scanner.*;


public abstract class Factor extends PascalSyntax {

	public Term tm;
	public Constant c;
	public Variable vb;
	public FuncCall fc;
	public InnerExp inexp;
	public Negation neg;
	public Negation negat;
	public static Factor fot = null;

	public Factor(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	 /**
     * Parse a Factor.
     * @param Scanner Tokens.
     * @return the Factor object of the parse tree.
     */

 static Factor parse(Scanner s) {
		// TODO Auto-generated method stub

		enterParser("factor");
		/*System.out.println("factor enter parser l");
		
		System.out.println("factor input"+ s.curToken.id+s.curToken.kind);*/
		switch (s.curToken.kind) {
		
		case constToken:
		fot = Constant.parse(s); break;
		case varToken:
			fot = Variable.parse(s); break; 
		case notToken:
			fot=Negation.parse(s); break;  
		case leftParToken:
			fot=InnerExp.parse(s); break; 
			
		case nameToken:
			/*System.out.println("factor stv l"+s.curToken.id);*/
			
			if (s.nextToken.kind == leftBracketToken)
				fot= Variable.parse(s);
			else if (s.nextToken.kind == leftParToken)
				fot=FuncCall.parse(s); 
			else if ((s.nextToken.kind != leftBracketToken )|| (s.nextToken.kind != leftParToken))
				fot= Variable.parse(s);
			else fot= Constant.parse(s);
				
			
			
			break;
		
		case stringValToken:
		/*System.out.println("factor stv"+s.curToken.kind);*/
		fot= Constant.parse(s);
			
			 break;
		case intValToken:
			/*System.out.println("factor int l"+s.curToken.id);*/
			fot= Constant.parse(s);
			 break;
		
		default : break;
		
		}
		leaveParser("factor");
		
		return fot;
		
		}
	
@Override
public String identify() {
	// TODO Auto-generated method stub
	return "<factor opr> " + " on line " + lineNum;
}

@Override
	void prettyPrint() {
		
	}

		
}