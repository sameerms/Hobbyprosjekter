package no.uio.ifi.pascal2100.parser;
import java.util.ArrayList;
import java.util.List;

import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.main.Main;

public class ProcCallStatm extends Statement {

	String name;
	/*String procName;*/
	Expression exp;
	Expression exp1;
	Expression firstexp;
	ProcDecl procRef;
	public  ArrayList <Expression>explist = new ArrayList<Expression>(); 
	
	public ProcCallStatm(int lNum) {
		super(lNum);
		// TODO Auto-generated constructor stub
	}

	@Override public String identify() {
		return "<proc call> on line " + lineNum;
								}
	
	
	
	


    /**
     * Parse a ProcCallStatm.
     * @param Scanner Tokens.
     * @return the ProcCallStatm object of the parse tree.
     * ---name -----( ---expression---,---)--
     */
	
	public static ProcCallStatm parse(Scanner s) {
		enterParser("proc call");
		
		ProcCallStatm pcs= new ProcCallStatm(s.curLineNum());
		/*System.out.println("proc call parser");*/
		s.test(nameToken);
		pcs.name = s.curToken.id;
		
		s.readNextToken();
		if(s.curToken.kind == leftParToken){
			s.skip(leftParToken);
			
			pcs.firstexp=Expression.parse(s);
			Expression tempexp=pcs.firstexp;
		
			while (s.curToken.kind == commaToken){
				s.skip(commaToken);
				tempexp.nextexp= tempexp=Expression.parse(s);
				
				}
		
				s.skip(rightParToken);
			}
			
		leaveParser("proc call");
		return pcs;
		}
	
@Override void prettyPrint() {
	Main.log.prettyPrint(name); 


	Expression localexp= firstexp;
	if (firstexp != null){
		Main.log.prettyPrint("(");

		while (localexp!=null){
			localexp.prettyPrint();

			localexp=localexp.nextexp;
			if(localexp != null)Main.log.prettyPrint(",");

			}
		Main.log.prettyPrint(")");
		}
	}

@Override
public void check(Block curScope, Library lib) {
	
	PascalDecl d = curScope.findDecl(name,this);
	
	procRef = (ProcDecl)d;
	
	Expression localexp= firstexp;
	if (firstexp != null){
		

		while (localexp!=null){
			localexp.check(curScope, lib);

			localexp=localexp.nextexp;
			

			}
		
		}
}
	
}
	

